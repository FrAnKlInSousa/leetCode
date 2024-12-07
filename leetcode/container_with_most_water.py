from typing import List


class ContainerWater:
    def container_water(self, columns) -> int:
        max_container = 0
        # this solution method is worse because the two for loop
        # in this case, the complexity in O notation is O(n²)
        for index, colum in enumerate(columns):
            for internal_index, internal_colum in enumerate(columns):
                distance = internal_index - index
                if colum > internal_colum:
                    area = internal_colum * distance
                else:
                    area = colum * distance
                if area > max_container:
                    max_container = area

        return max_container


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        for _ in heights:
            distance = right - left
            area = (
                distance * heights[left]
                if heights[left] < heights[right]
                else distance * heights[right]
            )

            if area > max_area:
                max_area = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


my_columns = [1,8,6,2,5,4,8,3,7]


s = Solution()
result = s.maxArea(my_columns)
print(f'resultado: {result}')
