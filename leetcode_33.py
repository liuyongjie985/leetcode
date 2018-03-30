class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        i = 0
        for x in nums:
            if target == x:
                index = i
                break;

            i += 1
        return index

