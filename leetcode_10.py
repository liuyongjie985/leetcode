# class Solution(object):
#     #     def isMatch(self, s, p):
#     #         """
#     #         :type s: str
#     #         :type p: str
#     #         :rtype: bool
#     #         """
#     #         length_s = len(s)
#     #         length_p = len(p)
#     #         if length_s > length_p:
#     #             return False
#     #
#     #         i = 0
#     #         j = 0
#     #
#     #         my_list = []
#     #
#     #         for x in xrange(length_p):
#     #             i = 0
#     #             while i < length_s:
#     #                 if p[x + i] != s[i]:
#     #                     break
#     #                 i += 1
#     #             return True
#     #
#     #         return False
#     #
#     #
#     # so = Solution()
#     # print so.isMatch("aa", "a")
#
#     def match(self, text, pattern):
#         if not pattern: return not text
#         first_match = bool(text) and pattern[0] in {text[0], '.'}
#         return first_match and self.match(text[1:], pattern[1:])

class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


so = Solution()
print so.isMatch("aab", "a*b")
