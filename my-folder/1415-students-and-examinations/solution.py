import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    schedule_df = students.merge(subjects, how='cross')

    count_df = examinations.groupby(
        ['student_id', 'subject_name']
        ).agg(attended_exams=('subject_name', 'count'))
    
    result_df = schedule_df.merge(
        count_df, on=['student_id', 'subject_name'], how='left'
        ).sort_values(by=['student_id', 'subject_name'])

    result_df['attended_exams'].fillna(0, inplace=True)

    return result_df
