"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a
container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
https://leetcode.com/problems/container-with-most-water/description/
"""

import pytest
from leetcode.container_with_most_water import Solution, ContainerWater


class TestContainerWithMostWater:
    @pytest.mark.parametrize(
        'columns,expected',
        [([8, 7, 2, 1], 7), ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)],
    )
    def test_container_with_most_water(self, columns, expected):
        s = Solution()
        result = s.maxArea(columns)
        assert result == expected

    @pytest.mark.parametrize(
        'columns,expected',
        [([8, 7, 2, 1], 7), ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)],
    )
    def test_container_with_most_water_2nd_option(self, columns, expected):
        c = ContainerWater()
        result = c.container_water(columns)
        assert result == expected
