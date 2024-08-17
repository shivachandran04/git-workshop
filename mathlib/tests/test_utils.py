from mathlib import Matrix
from mathlib.utils import *
import pytest

def test_validate_matrix():
    valid_matrix = [[1, 2], [3, 4]]
    assert validate_matrix(valid_matrix)

    invalid_matrix = [[1, 2], [3]]
    with pytest.raises(ValueError):
        validate_matrix(invalid_matrix)

# TODO: ALL - Implement tests for the rest of the utils functions
# Use the test_validate_matrix test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html