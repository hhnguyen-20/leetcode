import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result = animals[(animals['weight'] > 100)]
    return result.sort_values(by='weight', ascending=False)[['name']]
