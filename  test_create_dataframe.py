"""
This module is designed for importing a pandas data frame and
checking it for the following errors.
"""

import pandas as pd

def test_create_dataframe(data_frame, column_names):
    """
    Testing a given pandas.DataFrame for the following errors.
    Args:
        data_frame: a pandas.DataFrame
        column_names: list of expected column names
    Raises:
        - If the expected column names do not match with the columns of the data,
          Key Error is raised.
        - If the number of rows are less than 1 in the data,
          Value Error is raised.
        - If there are missing values in the data,
          Value Error is raised.
        - If a column includes more than one data type,
          Type Error is raised.
    Returns:
        "PASS" if no errors raised.
    """
    if list(data_frame.columns) != list(column_names):
        raise KeyError("Column names are not found")

    if len(data_frame.index) < 1:
        raise ValueError("There are not enough rows.")

    if data_frame.isnull().values.any():
        raise ValueError("There are missing values in the data")

    for i in list(column_names):
        if len(set(data_frame[i].apply(type))) != 1:
            raise TypeError("All values in the same column should be same data type")
    return print('PASS')


#calling the test_create_dataframe function:
URL = ('https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD')
SAMPLE_DF = pd.read_csv(URL)
EXPECTED_COLNAMES = SAMPLE_DF.columns
test_create_dataframe(SAMPLE_DF, EXPECTED_COLNAMES)
