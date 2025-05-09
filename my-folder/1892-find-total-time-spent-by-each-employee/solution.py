import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time'] = employees['out_time'] - employees['in_time']
    
    result = employees.groupby(['emp_id', 'event_day'])['time'].sum().reset_index()
    result.rename(columns={'event_day': 'day', 'time': 'total_time'}, inplace=True)
    
    return result
