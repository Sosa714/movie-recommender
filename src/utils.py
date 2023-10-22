import os

"""
Given a filename, returns the full path to the file located in the data directory.
"""
def get_data_path(filename):

    return os.path.join(os.getcwd(), 'data', filename)