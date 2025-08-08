import streamlit as st
import pandas as pd

from analysis import analyze_performance
from risk_predictor import predict_risk
from recommendation import give_recommendations
from visualizer import visualize_student

st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("🎓 Student Performance Dashboard")

st.markdown("""
Welcome to the **Student Performance Dashboard**. Upload student data (CSV file) with:
- Name
- Subject
- Marks
- Max_Marks
- Attendance_Percentage
""")

uploaded_file = st.file_uploader("📁 Upload student_data.csv", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    students = df['Name'].unique()
    selected_student = st.sidebar.selectbox("🔍 Select a Student", students)

    student_df = df[df['Name'] == selected_student]

    st.header(f"📊 Analysis for {selected_student}")

    col1, col2 = st.columns([2, 3])

    with col1:
        analysis_result = analyze_performance(student_df)
        risk = predict_risk(student_df)
        suggestions = give_recommendations(analysis_result, student_df)

        st.subheader("🧠 Weak Subjects")
        st.write(', '.join(analysis_result['weak_subjects']) or "None")

        st.subheader("⚠️ Risk of Failing")
        st.write("🔴 High" if risk else "🟢 Low")

        st.subheader("✅ Recommendations")
        for rec in suggestions:
            st.markdown(f"- {rec}")

    with col2:
        visualize_student(student_df, selected_student)
else:
    st.warning("Please upload a valid CSV file to continue.")
