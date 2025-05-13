import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee_department = employee.merge(
        department, left_on='departmentId', right_on='id')

    employee_department = employee_department[
        ['salary', 'departmentId', 'name_y']].drop_duplicates()
    
    top_salary = employee_department.groupby(
        ['name_y', 'departmentId'])['salary'].nlargest(3).reset_index()
    
    result = top_salary.merge(employee, on=['departmentId', 'salary'])
    
    result.rename(
        columns={'name_y': 'Department', 'name': 'Employee', 'salary': 'Salary'}, inplace=True)

    return result[['Department', 'Employee', 'Salary']]
