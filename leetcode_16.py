class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        close = 0

        first = True

        for x in xrange(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            l = x + 1
            r = len(nums) - 1
            while l < r:
                s = nums[x] + nums[l] + nums[r]
                if first == True:
                    first = False
                    close = self.getAbsolute(target - s)
                    sum = s
                else:
                    temp = self.getAbsolute(target - s)
                    if temp < close:
                        close = temp
                        sum = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1

                else:
                    return target
        return sum

    def getAbsolute(self, num):
        if num < 0:
            return 0 - num
        else:
            return num


so = Solution()
print so.threeSumClosest([-1, 2, 1, -4], 1)
