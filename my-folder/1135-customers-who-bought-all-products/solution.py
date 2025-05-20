import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby(
        'customer_id'
    ).agg(n_product=('product_key', 'nunique')).reset_index()

    return df[df['n_product'] == len(product)][['customer_id']]
