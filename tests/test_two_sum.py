import pytest

from leetcode.two_sum import two_sum_01, two_sum_02

"""
Two Sum

Given an array of integers 'nums' and an integer 'target',
return indices of the two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""


@pytest.mark.parametrize(
    ('nums', 'target', 'expected'),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_tow_sum_01(nums, target, expected):
    result = two_sum_01(nums, target)
    assert result == expected


@pytest.mark.parametrize(
    ('nums', 'target', 'expected'),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_tow_sum_02(nums, target, expected):
    result = two_sum_02(nums, target)
    assert result == expected
