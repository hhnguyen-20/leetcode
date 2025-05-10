import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager = employee.groupby('managerId').agg(
        reporting=('id', 'count')
    )
    
    result = manager.merge(
        employee[['id','name']], 
        left_on='managerId', 
        right_on='id', 
        how='inner')

    return result[result['reporting'] >= 5][['name']]
