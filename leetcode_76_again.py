# coding:utf-8
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if len(t) == 0:
            return ""

        words_map = {}
        target = 0
        for x in t:
            if words_map.has_key(x):
                words_map[x] += 1
            else:
                words_map[x] = 1
            target += 1
        left = 0
        count = 0

        min_length = len(s)
        min_index = []

        # 把left移动到包含字符的位置
        while left < len(s) and not words_map.has_key(s[left]):
            left += 1
        right = left

        while right < len(s):
            now_char = s[right]
            if words_map.has_key(now_char):
                words_map[now_char] -= 1
                if words_map[now_char] >= 0:
                    count += 1

                while count == len(t):
                    if right - left < min_length:
                        min_length = right - left
                        min_index = [left, right + 1]

                    if words_map.has_key(s[left]):
                        words_map[s[left]] += 1

                        if words_map[s[left]] > 0:
                            count -= 1

                    left += 1
            right += 1
        if len(min_index) == 0:
            return ""
        else:
            return s[min_index[0]: min_index[1]]


so = Solution()
print so.minWindow("ADOBECODEBANC", "ABC")
# print so.minWindow("a", "b")
# print so.minWindow("a", "aa")
# print so.minWindow("ab", "b")
# print so.minWindow("acbbaca", "aba")
