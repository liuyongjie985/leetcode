class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_list = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                      "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                      "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                      "", "M", "MM", "MMM", "MMMM"]
        return roman_list[num / 1000 + 30] + roman_list[num % 1000 / 100 + 20] + roman_list[num % 100 / 10 + 10] + \
               roman_list[num % 10]


so = Solution()
print so.intToRoman(412)
