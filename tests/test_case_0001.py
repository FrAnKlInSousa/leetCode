import pytest

from case_2133.case_0001.case_0001 import two_sum_01, two_sum_02


class TestTwoSum:
    @pytest.mark.parametrize("nums,target,expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ])
    def test_tow_sum_01(self, nums, target, expected):
        result = two_sum_01(nums, target)
        assert result == expected

    @pytest.mark.parametrize("nums,target,expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ])
    def test_tow_sum_02(self, nums, target, expected):
        result = two_sum_02(nums, target)
        assert result == expected


