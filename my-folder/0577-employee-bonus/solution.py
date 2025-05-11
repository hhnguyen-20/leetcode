import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    result_df = employee.merge(bonus, on='empId', how='left')

    result_df = result_df[(result_df['bonus'] < 1000) | result_df['bonus'].isnull()]

    return result_df[['name', 'bonus']]
