import os
import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import streamlit as st
import pandas as pd

# --- Build path to the model ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # dossier app/
model_path = os.path.join(BASE_DIR, "..", "model", "loan_logreg_l2_v1_20251125.joblib") 


# Vérification : existe-t-il ?
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Le fichier modèle est introuvable : {model_path}")

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
