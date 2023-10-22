import pandas as pd
from .utils import get_data_path

"""
Loads a CSV file from the data directory and returns a pandas DataFrame.
"""
def load_data(filename):

    return pd.read_csv(get_data_path(filename))

"""
Print basic statistics about the data.
"""
def basic_statistics(df):

    print("Head of the dataset:")
    print(df.head())

    print("\nShape of the dataset:", df.shape)

    print("\nGeneral information:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nUnique values (first 10 columns):")
    for col in df.columns[:10]:
        print(f"{col}: {len(df[col].unique())} unique values")