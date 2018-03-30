# coding:utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        mystr = s[::-1]

        return self.dynamicPrograming(s, mystr)

    def dynamicPrograming(self, str1, str2):
        length1 = len(str1)
        length2 = length1

        substring = ""
        max_length = 0
        matrix = []
        for x in xrange(length1):
            temp_list = []
            for y in xrange(length2):
                now = matrix[x - 1][y - 1] if x >= 1 and y >= 1 else 0
                if str1[x] == str2[y]:
                    temp_list.append(now + 1)

                    # if self.ispalindromic(str1[x - now:x + 1]) and len(str1[x - now:x + 1]) > max_length:
                    if now + 1 > max_length and self.ispalindromic(str1[x - now:x + 1], now + 1):
                        max_length = max(max_length, now + 1)
                        substring = str1[x - now:x + 1]


                else:
                    temp_list.append(0)
            matrix.append(temp_list)

        return substring

    def ispalindromic(self, s, length):
        i = 0
        while i < length / 2:
            if s[i] != s[length - i - 1]:
                return False
            i += 1
        return True


so = Solution()
print so.longestPalindrome("babad")
