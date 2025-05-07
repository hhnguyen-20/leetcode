import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cooperation = actor_director.groupby(['actor_id', 'director_id']).agg(
        time=('director_id', 'count')
    ).reset_index()

    return cooperation[cooperation['time'] >= 3][['actor_id', 'director_id']]

