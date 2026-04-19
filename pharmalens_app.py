import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os
import joblib

# =========================
# TITLE
# =========================
st.set_page_config(page_title="PharmaLens", layout="wide")
st.title("🧬 PharmaLens: Clinical Outcome Intelligence System")

st.write("Upload your clinical trial dataset and predict success probability using AI")

# =========================
# TRAIN MODEL (AUTO)
# =========================
MODEL_PATH = "model.pkl"

def train_model():
    data = {
        "phase": [1,2,3,1,2,3,2,1,3,2],
        "enrollment": [50,120,300,40,150,500,90,60,450,200],
        "duration": [6,12,24,5,14,36,10,8,30,18],
        "has_control": [0,1,1,0,1,1,1,0,1,1],
        "randomized": [0,1,1,0,1,1,0,1,1,1],
        "disease_area": [0,0,1,2,2,0,1,2,1,0],
        "sponsor_success_rate": [0.3,0.5,0.7,0.2,0.6,0.8,0.4,0.3,0.75,0.65],
        "outcome": [0,1,1,0,1,1,0,0,1,1]
    }

    df = pd.DataFrame(data)
    X = df.drop("outcome", axis=1)
    y = df["outcome"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    return model

# Load or train model
if not os.path.exists(MODEL_PATH):
    model = train_model()
else:
    model = joblib.load(MODEL_PATH)

# =========================
# SAMPLE DATA DOWNLOAD
# =========================
st.subheader("📥 Download Sample Dataset")

sample_data = pd.DataFrame({
    "phase": [1,2,3],
    "enrollment": [50,120,300],
    "duration": [6,12,24],
    "has_control": [0,1,1],
    "randomized": [0,1,1],
    "disease_area": ["oncology","cardio","cns"],
    "sponsor_success_rate": [0.3,0.5,0.7]
})

csv_sample = sample_data.to_csv(index=False).encode('utf-8')
st.download_button("Download Sample CSV", csv_sample, "sample_trials.csv")

# =========================
# FILE UPLOAD
# =========================
st.subheader("📤 Upload Your Dataset")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Uploaded Data")
    st.dataframe(df)

    # =========================
    # DATA PROCESSING
    # =========================
    mapping = {"oncology":0, "cardio":1, "cns":2}
    
    if "disease_area" in df.columns:
        df["disease_area"] = df["disease_area"].map(mapping)

    required_cols = [
        "phase","enrollment","duration",
        "has_control","randomized",
        "disease_area","sponsor_success_rate"
    ]

    if all(col in df.columns for col in required_cols):

        X = df[required_cols]

        # =========================
        # PREDICTION
        # =========================
        predictions = model.predict(X)
        probabilities = model.predict_proba(X)[:,1]

        df["Prediction"] = predictions
        df["Success_Probability"] = probabilities

        # Risk categorization
        def risk_label(p):
            if p > 0.7:
                return "High Success"
            elif p > 0.4:
                return "Moderate"
            else:
                return "High Risk"

        df["Risk_Category"] = df["Success_Probability"].apply(risk_label)

        # =========================
        # OUTPUT
        # =========================
        st.subheader("🔍 Prediction Results")
        st.dataframe(df)

        # Metrics
        st.subheader("📈 Summary")
        st.write("Average Success Probability:", round(df["Success_Probability"].mean(),2))
        st.write("High Success Trials:", sum(df["Risk_Category"]=="High Success"))
        st.write("High Risk Trials:", sum(df["Risk_Category"]=="High Risk"))

        # Download result
        csv_result = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇ Download Predictions", csv_result, "predictions.csv")

    else:
        st.error("Dataset must contain required columns!")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("⚡ Built for Pharma + Data Science Integration")
