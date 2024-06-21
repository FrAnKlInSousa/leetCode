import pytest

from leetcode.row_and_column_contain_all_num import (
    check_row_and_col_01,
    check_row_and_col_02,
    check_row_and_col_03,
)

"""
Check if Every Row and Column Contains All Numbers
https://leetcode.com/problems/c
heck-if-every-row-and-column-contains-all-numbers/description/
An n x n matrix is valid if every row and every column
contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix 'matrix', return true if
the matrix is valid. Otherwise, return false.
"""


@pytest.mark.parametrize(
    ('matrix', 'expected'),
    [
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),
    ],
)
def test_check_row_and_col_01(matrix, expected):
    result = check_row_and_col_01(matrix)
    assert result == expected


@pytest.mark.parametrize(
    ('matrix', 'expected'),
    [
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),
    ],
)
def test_check_row_and_col_v02(matrix, expected):
    result = check_row_and_col_02(matrix)
    assert result == expected


@pytest.mark.parametrize(
    ('matrix', 'expected'),
    [
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),
    ],
)
def test_check_row_and_col_v03(matrix, expected):
    result = check_row_and_col_03(matrix)
    assert result == expected
