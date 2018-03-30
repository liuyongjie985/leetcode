class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
            else:
                i += 1

        for i, x in enumerate(nums):
            if i != x - 1:
                return i + 1
            if i == len(nums) - 1:
                return i + 1 + 1


#
# class Solution(object):
#     def firstMissingPositive(self, nums):
#         i, n = 0, len(nums)
#         while i < n:
#             if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#                 # swap
#                 temp = nums[i]
#                 nums[i] = nums[nums[i] - 1]
#                 nums[temp - 1] = temp
#             else:
#                 i += 1
#         for i, v in enumerate(nums):
#             if v != i + 1:
#                 return  i + 1
#         return n + 1


so = Solution()
# print so.firstMissingPositive([1, 2, 0])
# print so.firstMissingPositive([])

# print so.firstMissingPositive([2, 3, 0])
# print so.firstMissingPositive([1,2, 3, 0])
# print so.firstMissingPositive([4, -1, 2, 3])
# print so.firstMissingPositive([3, 2])
print so.firstMissingPositive([1])
