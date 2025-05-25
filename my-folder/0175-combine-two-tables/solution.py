import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address, on='personId', how='left')

    return result[['firstName', 'lastName', 'city', 'state']]
