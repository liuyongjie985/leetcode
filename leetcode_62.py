class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.CMN(m, n)

    def factorial(self, num):
        result = 1
        for x in range(1,num+1):
            result *= x
        return result

    def CMN(self, m, n):
        return self.factorial(m + n - 2) / (self.factorial(n -1) * self.factorial(m-1))