import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("churn_model.pkl", "rb"))
columns = pickle.load(open("model_columns.pkl", "rb"))

st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("📊 Customer Churn Prediction System")
st.write("Enter customer details to predict churn risk")

tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 10.0, 150.0, 50.0)
fiber = st.selectbox("Fiber Internet?", ["Yes", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
tech = st.selectbox("Tech Support?", ["Yes", "No"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Auto Payment"])

input_data = {}

for col in columns:
    input_data[col] = 0

input_data["tenure"] = tenure
input_data["MonthlyCharges"] = monthly

if contract == "One year":
    input_data["Contract_One year"] = 1
elif contract == "Two year":
    input_data["Contract_Two year"] = 1

if fiber == "Yes":
    input_data["InternetService_Fiber optic"] = 1
else:
    input_data["InternetService_No"] = 1

if tech == "Yes":
    input_data["TechSupport_Yes"] = 1

if payment == "Electronic check":
    input_data["PaymentMethod_Electronic check"] = 1
elif payment == "Mailed check":
    input_data["PaymentMethod_Mailed check"] = 1

input_df = pd.DataFrame([input_data])

if st.button("Predict Churn"):
    prob = model.predict_proba(input_df)[0][1]

    if prob > 0.8:
        st.error(f"High Risk of Churn: {prob*100:.2f}%")
    elif prob > 0.5:
        st.warning(f"Medium Risk of Churn: {prob*100:.2f}%")
    else:
        st.success(f"Low Risk of Churn: {prob*100:.2f}%")
