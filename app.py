import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("models\jamb_score_predictor.pkl")

st.set_page_config(page_title="🎓 JAMB Score Predictor", layout="centered")
st.title("🎯 JAMB Performance Predictor")
st.markdown("Fill in your details to get a predicted JAMB score.")

# 📥 INPUTS

study_hours = st.slider("📚 Study Hours per Week", 0, 50, 15)
attendance_rate = st.slider("🏫 Attendance Rate (%)", 0, 100, 80)
teacher_quality = st.selectbox("👨‍🏫 Teacher Quality (1=Low, 5=High)", [1, 2, 3, 4, 5])
distance = st.number_input("📍 Distance to School (in km)", min_value=0.0, step=0.1, value=5.0)

school_type_label = st.selectbox("🏫 School Type", ["Public", "Private"])
school_type = 0 if school_type_label == "Public" else 1

school_location_label = st.selectbox("📌 School Location", ["Rural", "Urban"])
school_location = 0 if school_location_label == "Rural" else 1

extra_tutorials_label = st.selectbox("📖 Attends Extra Tutorials?", ["No", "Yes"])
extra_tutorials = 0 if extra_tutorials_label == "No" else 1

learning_materials_label = st.selectbox("📚 Access to Learning Materials?", ["No", "Yes"])
learning_materials = 0 if learning_materials_label == "No" else 1

parent_involvement_label = st.selectbox("👨‍👩‍👧 Parent Involvement", ["Low", "Medium", "High"])
parent_involvement = {"Low": 0, "Medium": 1, "High": 2}[parent_involvement_label]

it_knowledge_label = st.selectbox("💻 IT Knowledge", ["None", "Basic", "Advanced"])
it_knowledge = {"None": 0, "Basic": 1, "Advanced": 2}[it_knowledge_label]

age = st.slider("Age", 10, 30, 18)

gender_label = st.selectbox("👤 Gender", ["Male", "Female"])
gender = 0 if gender_label == "Male" else 1

socioeconomic_label = st.selectbox("💼 Socioeconomic Status", ["Low", "Medium", "High"])
socioeconomic = {"Low": 0, "Medium": 1, "High": 2}[socioeconomic_label]


parent_education_label = st.selectbox("🎓 Parent's Education Level", ["None", "Secondary", "University"])
parent_education = {"None": 0, "Secondary": 1, "University": 2}[parent_education_label]

assignments_done_label = st.selectbox("📝 Assignments Completed", ["None", "Few", "Most", "All"])
assignments_done = {"None": 0, "Few": 1, "Most": 2, "All": 3}[assignments_done_label]

# 🔄 COMBINE INPUTS

input_data = np.array([[
    study_hours,
    attendance_rate,
    teacher_quality,
    distance,
    school_type,
    school_location,
    extra_tutorials,
    learning_materials,
    parent_involvement,
    it_knowledge,
    age,
    gender,
    socioeconomic,
    parent_education,
    assignments_done
]])

# ---------------------
# 🔮 MAKE PREDICTION
# ---------------------
if st.button("🔍 Predict JAMB Score"):
    prediction = model.predict(input_data)
    st.success(f"🏆 Predicted JAMB Score: {round(prediction[0], 2)}")
