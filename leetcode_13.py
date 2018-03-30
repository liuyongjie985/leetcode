class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                      "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                      "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                      "", "M", "MM", "MMM", "MMMM"]
        for x in xrange(4000):
            roman = roman_list[x / 1000 + 30] + roman_list[x % 1000 / 100 + 20] + roman_list[x % 100 / 10 + 10] + \
                    roman_list[x % 10]
            if roman == s:
                return x

so = Solution()
print so.romanToInt("CMLII")