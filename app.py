import streamlit as st
import pickle
import pdfplumber

def get_precautions(risk_level):

    if risk_level == "High":
        return [
            "Consult a doctor immediately",
            "Monitor blood pressure regularly",
            "Check oxygen levels frequently",
            "Avoid heavy physical activity",
            "Drink enough water and rest"
        ]

    elif risk_level == "Medium":
        return [
            "Maintain healthy diet",
            "Exercise regularly",
            "Monitor health daily",
            "Reduce stress",
            "Sleep properly"
        ]

    else:
        return [
            "Maintain healthy lifestyle",
            "Exercise regularly",
            "Eat balanced food",
            "Routine health checkups"
        ]
model = pickle.load(open("model.pkl","rb"))

st.set_page_config(page_title="Care AI", page_icon="🩺")

st.title("🩺 Care AI - Health Risk Predictor")
st.write("Enter patient health data to predict risk level")

uploaded_file = st.file_uploader("Upload Medical Report", type=["pdf","txt","jpg","png","jpeg"])

if uploaded_file is not None:

    text = ""

    if uploaded_file.type == "application/pdf":

        import pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()

        st.write("Medical Report Content:")
        st.write(text)

    else:
        st.success("Medical report uploaded successfully")

st.sidebar.header("Patient Details")

heart_rate = st.sidebar.number_input("Heart Rate")
bp = st.sidebar.number_input("Blood Pressure")
oxygen = st.sidebar.number_input("Oxygen Level")
temp = st.sidebar.number_input("Temperature")

if st.sidebar.button("Predict Risk"):

    prediction = model.predict([[heart_rate,bp,oxygen,temp]])

    risk = prediction[0]

    if prediction[0] == "High":
        st.error("⚠ High Risk - Immediate Attention Required")

    elif prediction[0] == "Medium":
        st.warning("⚠ Medium Risk - Monitor Patient")

    else:
        st.success("✅ Low Risk - Patient Stable") 

    precautions = get_precautions(risk)

    st.subheader("Precautions / Suggestions")

    for p in precautions:
        st.write("•", p)


def get_precautions(risk_level):

    if risk_level == "High":
        return [
            "Consult a doctor immediately",
            "Monitor blood pressure regularly",
            "Check oxygen levels frequently",
            "Avoid heavy physical activity",
            "Drink enough water and take rest"
        ]

    elif risk_level == "Medium":
        return [
            "Maintain healthy diet",
            "Exercise regularly",
            "Monitor health parameters daily",
            "Reduce stress",
            "Get enough sleep"
        ]

    else:
        return [
            "Maintain healthy lifestyle",
            "Exercise regularly",
            "Eat balanced food",
            "Regular health checkups"
        ]