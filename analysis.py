def analyze_performance(student_df):
    weak_subjects = []
    for _, row in student_df.iterrows():
        percentage = (row['Marks'] / row['Max_Marks']) * 100
        if percentage < 40:
            weak_subjects.append(row['Subject'])

    return {
        'weak_subjects': weak_subjects
    }
