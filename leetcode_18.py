class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()

        re = []

        for x in xrange(len(nums) - 3):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            y = x + 1
            while y < len(nums) - 2:
                l = y + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[x] + nums[y] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    else:
                        re.append([nums[x], nums[y], nums[l], nums[r]])
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                y += 1
                while y < len(nums) - 2 and nums[y] == nums[y - 1]:
                    y += 1
        return re if len(re) > 0 else []


so = Solution()
print so.fourSum([0, 0, 0, 0], 0)
