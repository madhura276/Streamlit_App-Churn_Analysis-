#  Customer Churn Prediction System

An end-to-end Machine Learning web application that predicts customer churn risk in real time using a trained classification model deployed via Streamlit.

---

## Live Demo
watch here : https://customer-churn-prediction-system-ab7dxjlk5eo7ptady7hmut.streamlit.app/

## Overview

Customer churn is one of the most critical business problems in the telecom industry. This system allows businesses to identify at-risk customers before they leave — enabling proactive retention strategies.

The application takes customer details as input, runs them through a pre-trained ML model, and outputs a **churn probability** along with a **risk classification** (High / Medium / Low).

---

## Machine Learning Approach

- **Algorithm:** Logistic Regression / XGBoost (trained model saved as `churn_model.pkl`)
- **Feature Engineering:** One-hot encoding of categorical variables (Contract type, Internet Service, Payment Method, Tech Support)
- **Input Features:**
  - Tenure (months)
  - Monthly Charges
  - Internet Service type (Fiber optic / No)
  - Contract type (Month-to-month / One year / Two year)
  - Tech Support availability
  - Payment Method
- **Output:** Churn probability score with risk classification
  -  High Risk → probability > 80%
  -  Medium Risk → probability between 50%–80%
  -  Low Risk → probability < 50%

---

##  Key Features

- Real-time churn prediction via interactive web UI
- Probability-based risk classification (High / Medium / Low)
- Clean and intuitive Streamlit interface
- Pre-trained model loaded directly — no retraining required
- Supports multiple contract and payment scenarios

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| ML Libraries | Scikit-learn, XGBoost, Pandas |
| Model Serialization | Pickle |
| Web App | Streamlit |
| Data Handling | Pandas, NumPy |

---

##  Project Structure

```
Customer-Churn-Prediction-System/
│
├── app.py                  # Streamlit web application
├── churn_model.pkl         # Pre-trained ML classification model
├── model_columns.pkl       # Feature columns used during training
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

##  How to Run Locally

### Prerequisites
- Python 3.8 or above
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/madhura276/Customer-Churn-Prediction-System.git
cd Customer-Churn-Prediction-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

```
http://localhost:8501
```

---

##  How to Use

1. Open the app in your browser
2. Enter customer details using the input fields:
   - Adjust **Tenure** using the slider
   - Enter **Monthly Charges**
   - Select **Internet Service**, **Contract Type**, **Tech Support**, and **Payment Method**
3. Click **Predict Churn**
4. View the churn probability and risk classification instantly

---

##  Input Features Explained

| Feature | Description |
|---|---|
| Tenure (Months) | How long the customer has been with the company |
| Monthly Charges | The amount charged to the customer per month |
| Fiber Internet | Whether the customer uses fiber optic internet |
| Contract Type | Month-to-month, One year, or Two year contract |
| Tech Support | Whether the customer has tech support enabled |
| Payment Method | Electronic check, Mailed check, or Auto Payment |

---

##  Risk Classification

| Risk Level | Churn Probability | Action Recommended |
|---|---|---|
|  High Risk | > 80% | Immediate retention intervention |
|  Medium Risk | 50% – 80% | Proactive outreach and offers |
|  Low Risk | < 50% | Monitor regularly |

---

##  Future Improvements

- Add SHAP-based model explainability to show feature importance per prediction
- Integrate a live database for batch customer churn analysis
- Add Power BI dashboard link for business-level reporting
- Enable CSV upload for bulk churn prediction
- Deploy on Streamlit Cloud or AWS for public access

---

##  Requirements

Create a `requirements.txt` file with the following:

```
streamlit
pandas
numpy
scikit-learn
xgboost
pickle5
```

##  License

MIT

---

> **Disclaimer:** Predictions are generated using ML-based probability estimation and are intended to support business decisions, not replace them.
