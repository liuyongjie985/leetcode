class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        re = []
        nums.sort()

        self.getNSum(4, nums, target, re, [])

        return re

    def getNSum(self, N, nums, target, re, result):
        if N < 2:
            return
        if N == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s > target:
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    re.append(result + [nums[l], nums[r]])
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        if N > 2:

            i = 0
            while i < len(nums) - N + 1:
                if nums[i] * N > target or nums[-1] * N < target:
                    break

                if i > 0 and nums[i] == nums[i - 1]:
                    i += 1
                    continue

                self.getNSum(N - 1, nums[i + 1:], target - nums[i], re, result + [nums[i]])
                i += 1


so = Solution()
print so.fourSum([1, 0, -1, 0, -2, 2], 0)
