def give_recommendations(analysis_result, student_df):
    recommendations = []
    if analysis_result['weak_subjects']:
        for subject in analysis_result['weak_subjects']:
            rec = f"Focus on {subject}: Revise concepts, practice questions."
            recommendations.append(rec)

    if student_df['Attendance_Percentage'].mean() < 75:
        recommendations.append("Improve attendance to at least 80% for better understanding.")

    return recommendations
