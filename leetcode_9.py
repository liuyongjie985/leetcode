class Solution(object):
    def intlength(self, inte):
        if inte == 0:
            return 1
        count = 0
        while inte != 0:
            inte = inte / 10
            count += 1
        return count

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        origin = x
        reversed_num = 0
        if x < 0:
            return False
        if self.intlength(x) == 1:
            return True
        count = 0
        while reversed_num < x:
            reversed_num = reversed_num * 10 + x % 10
            x = x / 10
            count += 1

        if self.intlength(reversed_num) + self.intlength(x) != self.intlength(origin):
            return False

        if self.intlength(reversed_num) == self.intlength(x):
            if reversed_num == x:
                return True
            else:
                return False
        else:
            reversed_num = reversed_num / 10
            if reversed_num == x:
                return True
            else:
                return False


so = Solution()
print so.isPalindrome(21120)
