import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(values='temperature',
                               columns='city',
                               index='month',
                               )
