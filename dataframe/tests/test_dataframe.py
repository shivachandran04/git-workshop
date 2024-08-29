from dataframe import DataFrame
import pytest

def test_df_vertical_concat():
    df1 = DataFrame(data=[[1, 2], [3, 4]], columns=["A", "B"])
    df2 = DataFrame(data=[[5, 6], [7, 8]], columns=["C", "D"])
    
    df1.concatenate_vertically(df2)
    assert df1.data == [[1, 2], [3, 4], [5, 6], [7, 8]]

# TODO: ALL - Implement tests for all other DataFrame methods
# Use the test_df_vertical_concat test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html