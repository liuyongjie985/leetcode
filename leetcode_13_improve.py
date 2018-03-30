class Solution(object):
    def getNumber(self, s, start, end, roman_map):
        while roman_map[s[start]] < roman_map[s[end]] and start > -1:
            start -= 1
        return s[start + 1:end + 1], start - 1, start

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_map = {"": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
                     "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
                     "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800,
                     "CM": 900, "M": 1000, "MM": 2000, "MMM": 3000, "MMMM": 4000}

        if len(s) < 2:
            return roman_map[s]

        start = len(s) - 2
        end = start + 1

        total = 0

        while start >= -1:
            my_str, start, end = self.getNumber(s, start, end, roman_map)
            total += int(roman_map[my_str])

        return total


so = Solution()
print so.romanToInt("CMLII")
