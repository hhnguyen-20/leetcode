import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates()

    sorted_salaries = distinct_salaries.sort_values(ascending=False)

    if N > len(sorted_salaries) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    else:
        nth_highest_salary = sorted_salaries.iloc[N - 1]
        return pd.DataFrame({f'getNthHighestSalary({N})' : [nth_highest_salary]})


