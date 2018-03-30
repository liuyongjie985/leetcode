class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        j = 0
        length = 0
        n = len(s)
        mymap = {}
        while i < n and j < n:
            if mymap.has_key(s[j]):
                mymap.pop(s[i])
                i += 1
            else:
                mymap[s[j]] = 1
                j += 1
                length = max(length, j - i)


        return length

re = Solution()
print re.lengthOfLongestSubstring("")

