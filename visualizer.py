import matplotlib.pyplot as plt
import streamlit as st

def visualize_student(student_df, student_name):
    subjects = student_df['Subject']
    marks = student_df['Marks']
    max_marks = student_df['Max_Marks']

    fig, ax = plt.subplots()
    ax.bar(subjects, marks, label='Marks')
    ax.plot(subjects, max_marks, color='red', linestyle='--', label='Max Marks')
    ax.set_title(f'Marks of {student_name}')
    ax.set_ylabel('Marks')
    ax.legend()
    st.pyplot(fig)
