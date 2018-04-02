class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        i = 0
        max = nums[0]
        if max >= len(nums) - 1:
            return True
        while i <= max:
            if i + nums[i] > max:
                max = i + nums[i]
                if max >= len(nums) - 1:
                    return True
            i += 1
        return False


so = Solution()
# print so.canJump([2, 3, 1, 1, 4])
# print so.canJump([3, 2, 1, 0, 4])

print so.canJump([1, 2, 3])
