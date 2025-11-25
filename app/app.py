import streamlit as st
import pandas as pd
import joblib
import os

# --- Load the model ---
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "loan_logreg_l2_v1_20251125.pkl")
model = joblib.load(model_path)

st.title("🏦 Loan Approval Prediction App")
st.write("Application professionnelle de scoring pour évaluer la solvabilité d'un client.")

# --- Formulaire utilisateur ---
st.header("📋 Informations du client")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Co-applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Amount Term", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# --- Conversion en DataFrame ---
input_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area]
})

# --- Prediction ---
if st.button("🔍 Predict Loan Approval"):
    prob = model.predict_proba(input_data)[0][1]
    pred = model.predict(input_data)[0]

    st.subheader("📊 Résultat")
    st.metric("Probabilité d'approbation", f"{prob*100:.2f}%")

    if pred == 1:
        st.success("✅ Crédit accepté")
    else:
        st.error("❌ Crédit refusé")
