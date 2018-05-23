# coding:utf-8

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        if k > n:
            return []
        if k == n:
            return [[x + 1 for x in xrange(n)]]
        result = []
        if k == 1:
            temp = [x + 1 for x in xrange(n)]
            for i, x in enumerate(temp):
                result.append([temp[i]])
            return result

        left_result = self.combine(n - 1, k - 1)
        right_result = self.combine(n - 1, k)
        for x in left_result:
            x.append(n)

        return left_result + right_result


so = Solution()
print so.combine(4, 2)
