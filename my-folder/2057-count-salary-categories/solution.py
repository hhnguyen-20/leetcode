import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = avg_count = high_count = 0

    for income in accounts["income"].tolist():
        if income < 20000:
            low_count += 1
        elif income <= 50000:
            avg_count += 1
        else:
            high_count += 1

    data = [
        ['Low Salary', low_count], 
        ['Average Salary', avg_count], 
        ['High Salary', high_count]
    ]

    df = pd.DataFrame(data, columns=['category', 'accounts_count'])

    return df
