# PharmaLens
<img width="1843" height="660" alt="Screenshot 2026-04-19 210832" src="https://github.com/user-attachments/assets/6e863933-c73c-460c-b2bd-26d3bf5b0020" />
<img width="1817" height="688" alt="Screenshot 2026-04-19 210847" src="https://github.com/user-attachments/assets/555fa056-b9fa-47f6-be8f-4b61d9c5d133" />
<img width="1799" height="844" alt="Screenshot 2026-04-19 210914" src="https://github.com/user-attachments/assets/0ff64fe9-0b29-45c0-89b8-c4ed69be8d54" />





# 🧬 PharmaLens: Translational Intelligence for Clinical Outcome Forecasting

PharmaLens is a data-driven predictive system designed to estimate the probability of success in clinical trials using structured clinical and sponsor-level features. This project integrates pharmaceutical domain knowledge with machine learning to support early-stage decision-making in drug development.

---

## 🚀 Overview

Clinical trials are expensive and time-consuming, with high failure rates across phases. PharmaLens provides a predictive framework that:

* Estimates trial success probability
* Classifies risk levels (High Risk / Moderate / High Success)
* Enables batch predictions via CSV upload
* Offers a simple and interactive user interface

---

## 🧠 Key Features

* 📊 **Batch Prediction** via CSV file upload
* ⚡ **Real-Time Inference** using trained ML model
* 🎯 **Probability Scoring** (0–1 success likelihood)
* 🔍 **Risk Categorization** for decision support
* ⬇ **Downloadable Results** for further analysis

---

## 🏗️ Project Structure

```
pharmalens/
│
├── app.py                 # Main Streamlit application
├── model.pkl              # Trained ML model (auto-generated)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 📊 Input Features

| Feature              | Description                    |
| -------------------- | ------------------------------ |
| phase                | Clinical trial phase (1, 2, 3) |
| enrollment           | Number of participants         |
| duration             | Trial duration (months)        |
| has_control          | Control group (0/1)            |
| randomized           | Randomization applied (0/1)    |
| disease_area         | oncology / cardio / cns        |
| sponsor_success_rate | Historical success rate (0–1)  |

---

## 📈 Output

* **Prediction**:

  * 0 → Likely Failure
  * 1 → Likely Success

* **Success Probability** (0–1)

* **Risk Category**:

  * High Risk
  * Moderate
  * High Success

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/pharmalens.git
cd pharmalens
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Application

```
streamlit run app.py
```

---

## 🧪 Usage

1. Launch the application
2. Download the sample dataset
3. Upload your CSV file
4. View predictions instantly
5. Download results

---

## ☁️ Deployment

This project can be deployed using:

* Streamlit Cloud
* Render
* Docker (optional for production)

---

## 🔬 Methodology

* Data preprocessing and encoding
* Feature-based modeling
* Random Forest classification
* Probability estimation using ensemble learning

---

## 💡 Future Enhancements

* Integration with real-world datasets (ClinicalTrials.gov)
* NLP analysis of trial descriptions
* Explainable AI (SHAP)
* Deep learning models (BERT + tabular fusion)
* API-based deployment

---

## 🎯 Applications

* Pharma R&D decision support
* Clinical trial risk assessment
* Portfolio prioritization
* Drug development strategy

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. Predictions are based on simulated and structured datasets and should not be used for real clinical decision-making.

---

## 👤 Author

Mayuresh Pathak
(B.Pharm + Data Science)

---

## ⭐ Acknowledgment

Inspired by challenges in clinical trial attrition and the need for data-driven pharmaceutical innovation.

---
