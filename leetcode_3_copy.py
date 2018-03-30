class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        mymap = {}
        for x in s:
            if mymap.has_key(x):
                mymap[x] += 1
            else:
                mymap[x] = 1

        total = len(mymap)

        i = total
        while i >= 1:
            if self.myfunc(total, len(s), s) == True:
                return total

            total -= 1
    def myfunc(self, num, length, s):
        i = 0

        while i <= (length - num):
            little_map = {}
            j = i
            while j < num+i:
                little_map[s[j]] = 1
                j += 1
            what = len(little_map)
            if what == num:
                return True

            i += 1
        return False

re = Solution()
print re.lengthOfLongestSubstring("enuyazszxldyujzvucidbxqcxiiqjifnxbozbiyatdzqpaljevpisfksovkxfqmctcdumdviiwyxwljcgykadvsrsdqx")
