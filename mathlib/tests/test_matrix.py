from mathlib import Matrix

def test_matrix_addition():
    matrix1 = Matrix(data=[[1, 2], [3, 4]])
    matrix2 = Matrix(data=[[5, 6], [7, 8]])
    result = matrix1 + matrix2
    assert result.data == [[6, 8], [10, 12]]

# TODO: ALL - Implement tests for all other Matrix methods
# Use the test_matrix_addition test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html