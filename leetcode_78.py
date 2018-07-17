class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 0:
            return []
        result = []
        self.algorithm(nums, result)

        return result

    def algorithm(self, sub_nums, result):
        if len(sub_nums) == 1:
            result.append([])
            result.append([sub_nums[0]])
            return

        self.algorithm(sub_nums[:len(sub_nums) - 1], result)
        right = []
        for x in result:
            a = list(x)
            a.append(sub_nums[-1])
            right.append(a)

        result += right
        return


so = Solution()
print so.subsets([1, 2, 3])
