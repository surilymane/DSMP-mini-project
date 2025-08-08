def predict_risk(student_df):
    avg_marks = student_df['Marks'].mean()
    avg_attendance = student_df['Attendance_Percentage'].mean()

    if avg_marks < 40 or avg_attendance < 75:
        return True
    return False
