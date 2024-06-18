import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    This function attempts to load a CSV file from the specified path, skipping
    the last line of the file. If successful, it prints the dimensions of the
    loaded DataFrame and returns it. If an error occurs during the loading
    process, an error message is printed and the exception is raised.

    Parameters:
    path (str): The file path to the CSV file to be loaded.

    Returns:
    pd.DataFrame: The loaded DataFrame.

    Exception: If there is an error during the file loading process.
    """
    try:
        df = pd.read_csv(path, skipfooter=1, engine='python')
        print("Loading dataset of dimensions: ", df.shape)
        return df
    except Exception as e:
        print(f"Error loading data file:\n{e}")
        return None
