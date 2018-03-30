class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        return self.factorial(n, x)

    def factorial(self, target, value):
        if target <= 1:
            return value
        if target == 2:
            return value * value

        half = self.factorial(target / 2, value)

        if target % 2 == 0:
            return half * half
        else:
            return half * half * value


so = Solution()
print so.myPow(3.0, 5)
