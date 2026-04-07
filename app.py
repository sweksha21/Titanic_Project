import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="centered")

# -----------------------------
# Title & Description
# -----------------------------
st.title("🚢 Titanic Survival Prediction App")
st.markdown("""
This app predicts whether a passenger would **survive or not** based on input features using a **Logistic Regression model**.

👉 Enter the passenger details below and click **Predict**
""")

# -----------------------------
# Sidebar Info (for explanation)
# -----------------------------
st.sidebar.header("📘 About Model")
st.sidebar.write("""
- Model: Logistic Regression  
- Dataset: Titanic Dataset  
- Target: Survival (0 = No, 1 = Yes)

Key Factors:
- Gender
- Passenger Class
- Fare
""")

# -----------------------------
# Input Section
# -----------------------------
st.subheader("🧾 Enter Passenger Details")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.slider("Age", 1, 80)

with col2:
    sibsp = st.number_input("Siblings/Spouses", 0, 10)
    parch = st.number_input("Parents/Children", 0, 10)
    fare = st.number_input("Fare", 0.0, 500.0)

embarked = st.selectbox("Embarked Port", ["S", "C", "Q"])

# -----------------------------
# Encoding (same as training)
# -----------------------------
sex_val = 1 if sex == "female" else 0
embarked_C = 1 if embarked == "C" else 0
embarked_Q = 1 if embarked == "Q" else 0

# Input array
input_data = np.array([[pclass, sex_val, age, sibsp, parch, fare, embarked_C, embarked_Q]])

# -----------------------------
# Prediction
# -----------------------------
st.markdown("---")

if st.button("🔍 Predict Survival"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.success(f"✅ Passenger is likely to SURVIVE\n\nProbability: {probability:.2f}")
    else:
        st.error(f"❌ Passenger is NOT likely to survive\n\nProbability: {probability:.2f}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
