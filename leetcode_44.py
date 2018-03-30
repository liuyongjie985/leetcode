class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i = 0
        j = 0
        i_max = len(s)


        new_p = ""

        pre = ""
        for x in p:
            if x == "*":
                if pre == "*":
                    continue
                else:
                    new_p = new_p + x
                    pre = x
            else:
                new_p = new_p + x
                pre = x
        j_max = len(new_p)
        return self.isvalid(i, i_max, j, j_max, s, new_p)

    def isvalid(self, i, i_max, j, j_max, s, p):

        if i >= i_max and j >= j_max:
            return True
        if i >= i_max:
            # while j < j_max and p[j] == '*':
            #     j += 1
            # if j >= j_max:
            if j == len(p) - 1 and p[j] == "*":
                return True

            return False
        if j >= j_max:
            return False

        if p[j] != '*':
            if s[i] == p[j] or p[j] == '?':
                return True and self.isvalid(i + 1, i_max, j + 1, j_max, s, p)
            else:
                return False
        else:
            while i <= i_max:
                if self.isvalid(i, i_max, j + 1, j_max, s, p) == True:
                    return True
                i += 1
            return False


so = Solution()
# print so.isMatch("aa", "a")
# print so.isMatch("aa", "aa")
# print so.isMatch("aaa", "aa")
# print so.isMatch("aa", "*")
# print so.isMatch("aa", "a*")
# print so.isMatch("ab", "?*")
#
# print so.isMatch("aab", "c*a*b")

# print so.isMatch("", "*")
# print so.isMatch("aa", "a*")
# print so.isMatch("leetcode", "*e*t?d*")
# print so.isMatch("ho", "ho**")
print so.isMatch("aaaa", "***a")
