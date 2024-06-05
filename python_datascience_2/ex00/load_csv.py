import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, skipfooter=1, engine='python')
        print("Loading dataset of dinensions: ", df.shape)
        return df
    except Exception as e:
        print(f"Error loading data file:\n{e}")
        return None
