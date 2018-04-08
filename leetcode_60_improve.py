class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        my_str = ""
        for x in xrange(n):
            my_str += str(x + 1)

        return self.getTH(n, k, my_str)

    def factorial(self, n):
        result = 1
        for x in xrange(n):
            result *= x + 1
        return result

    def getTH(self, n, k, sub_str):
        if n == 1:
            return sub_str

        if n == 2:
            if k != 1:

                return sub_str[::-1]
            else:
                return sub_str
        f = self.factorial(n - 1)
        a = k % f
        b = k / f

        if a == 0:
            return sub_str[b - 1] + (sub_str[:b - 1] + sub_str[b:])[::-1]
        else:
            return sub_str[b] + self.getTH(n - 1, a, (sub_str[:b] + sub_str[b + 1:]))


so = Solution()
print so.getPermutation(4, 16)
