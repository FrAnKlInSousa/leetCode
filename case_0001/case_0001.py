from typing import List


def two_sum_01(nums: List[int], target: int) -> list[int]:
    for i in list(range(len(nums))):
        for j in list(range(i + 1, len(nums))):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_02(nums, target):
    n = len(nums)
    results = {}

    for i in range(n):
        complement = target - nums[i]
        if complement in results:
            return [results[complement], i]
        results[nums[i]] = i
    return []
