import pandas as pd
from utils import get_data_path

"""
    Loads a CSV file from the data directory and returns a pandas DataFrame.
"""
def load_data(filename):

    return pd.read_csv(get_data_path(filename))