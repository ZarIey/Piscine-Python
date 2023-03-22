import pandas as pd
import sys as check


def load(path: str) -> str:
    '''Load a .csv file and return it'''
    try:
        df = pd.read_csv(path)
        num_rows, num_cols = df.shape
        print(f'Loading dataset of dimensions ({num_rows}, {num_cols})')
    except (FileNotFoundError, UnboundLocalError, ValueError,
            IsADirectoryError, OSError):
        print("Error: something went wrong with the file 🤓")
        check, exit()
    return df
