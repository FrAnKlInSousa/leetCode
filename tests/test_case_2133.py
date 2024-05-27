import pytest

from case_2133.case_2133 import solution_01, solution_03, solution_02


class TestCheckRowAndCol:
    @pytest.mark.parametrize("matrix,expected", [
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True)
    ])
    def test_check_row_and_col_v01(self, matrix, expected):
        result = solution_01(matrix)
        assert result == expected

    @pytest.mark.parametrize("matrix,expected", [
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True)
    ])
    def test_check_row_and_col_v02(self, matrix, expected):
        result = solution_02(matrix)
        assert result == expected

    @pytest.mark.parametrize("matrix,expected", [
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True)
    ])
    def test_check_row_and_col_v03(self, matrix, expected):
        result = solution_03(matrix)
        assert result == expected