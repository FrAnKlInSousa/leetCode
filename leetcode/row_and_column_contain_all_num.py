from typing import List


def check_row_and_col_01(matrix: List[List[int]]) -> bool:
    row_len = len(matrix[0])

    for index_row, row in enumerate(matrix):
        row_set = set(row)
        expected_set = set(list(range(1, row_len + 1)))
        if row_set != expected_set:
            return False
        if len(matrix) != row_len:
            return False
        cols = set()
        for index_col, _ in enumerate(row):
            cell = matrix[index_col][index_row]
            cols.add(cell)

        if cols != expected_set:
            return False
    return True


def check_row_and_col_02(matrix: List[List[int]]) -> bool:
    matrix_len = len(matrix)
    for row, col in zip(matrix, zip(*matrix)):
        if len(set(row)) != matrix_len or len(set(col)) != matrix_len:
            return False
    return True


def check_row_and_col_03(matrix: List[List[int]]) -> bool:
    matrix_len = len(matrix)
    return not any(
        matrix_len != len(set(row)) or matrix_len != len(set(col))
        for row, col in zip(matrix, zip(*matrix))
    )
