import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    result = cinema[(cinema['id'] % 2 != 0) & (cinema['description'] != 'boring')]

    return result.sort_values(by='rating', ascending=False)
