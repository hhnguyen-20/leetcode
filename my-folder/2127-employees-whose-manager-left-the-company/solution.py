import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employee_id_list = employees['employee_id'].unique()

    result = employees[
        (employees['salary'] < 30000) & 
        ~(employees['manager_id'].isin(employee_id_list))
        ].dropna()

    result.sort_values(by='employee_id', inplace=True)

    return result[['employee_id']]
