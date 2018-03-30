class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        start = nums[0]
        i = 0
        num = 0
        while i < len(nums) - 1:
            i, max = self.isReach(i, start, len(nums), nums)
            num += 1
            start = max
        return num

    def isReach(self, start, steps, end, nums):
        max = nums[start]
        max_i = start
        if max == 1:
            return start + 1, nums[start + 1]

        i = 1
        # max_i = start + 1
        if start + steps >= end - 1:
            return end - 1, -1

        another_max = max
        # another_max_i = start + 1

        while i <= steps:
            if another_max < nums[start + i] + i:
                another_max = nums[start + i] + i
                max = nums[start + i]
                max_i = start + i
            i += 1

        if max_i == start:
            max = nums[start + steps]
            max_i = start + steps

        return max_i, max


so = Solution()
# print so.jump([2, 3, 1, 1, 4])
# print so.jump([1, 1, 1, 1])
# print so.jump([1, 2, 1, 1, 1])

# print so.jump([4, 1, 1, 3, 1, 1, 1])
print so.jump([2, 2, 0, 1])
