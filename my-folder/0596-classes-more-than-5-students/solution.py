import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    student_counting = courses.groupby(
        'class'
    ).agg(counting=('student', 'count')).reset_index()

    return student_counting[student_counting['counting'] >= 5][['class']]
