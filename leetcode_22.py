class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        self.iteration('', 0, 0, n, list)
        return list

    def iteration(self, str, left, right, max, list):
        if len(str) == max * 2:
            list.append(str)

        if left < max:
            self.iteration(str + '(', left + 1, right, max, list)

        if left > right:
            self.iteration(str + ")", left, right + 1, max, list)


so = Solution()
print so.generateParenthesis(3)
