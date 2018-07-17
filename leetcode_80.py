class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = -1
        count = 0
        length = 0
        index = 0
        for x in nums:
            nums[index] = x
            if now != x:
                count = 1
                now = x
            else:
                count += 1
            if count <= 2:
                length += 1
            else:
                index -= 1
            index += 1
        return length


so = Solution()
# print so.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
re = [1, 1, 1, 2, 2, 3]
print so.removeDuplicates(re)
print re
