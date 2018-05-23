# coding:utf-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0
        r = 0
        while i < len(nums) - r:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
            else:
                if nums[i] == 2:
                    temp = nums[i]
                    nums[i] = nums[len(nums) - 1 - r]
                    nums[len(nums) - 1 - r] = temp
                    r += 1
                    i -= 1
            i += 1


so = Solution()
# a = [2, 0, 2, 1, 1, 0]
a = [2, 0, 1]
so.sortColors(a)
print a
