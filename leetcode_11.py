class Solution(object):
    def getAbsolute(self, left, right):
        return left - right if left > right else right - left

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
                max_area = max(max_area, min(height[left], height[right]) * (right - left))
            else:
                right -= 1
                max_area = max(max_area, min(height[left], height[right]) * (right - left))
        return max_area

so =Solution()
print so.maxArea([2,3,6,4])