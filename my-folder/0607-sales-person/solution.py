import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = orders.merge(company, on='com_id')
    
    red_sales_id_list = merged_df[merged_df['name'] == 'RED']['sales_id'].unique()
    
    return sales_person[~(sales_person['sales_id'].isin(red_sales_id_list))][['name']]

