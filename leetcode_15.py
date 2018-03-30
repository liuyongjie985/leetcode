class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        re = []

        for x in xrange(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            l = x + 1
            r = len(nums) - 1
            while l < r:
                s = nums[x] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    re.append([nums[x], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return re


so = Solution()
print so.threeSum([0, 0, 0])
