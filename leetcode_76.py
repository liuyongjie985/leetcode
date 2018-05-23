class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        word_map = {}
        index_map = {}
        index_list = []

        for x in t:
            if word_map.has_key(x):
                word_map[x] += 1
            else:
                word_map[x] = 1

        min_dis = 99999999999
        min_start = -1
        min_end = -1
        for i, x in enumerate(s):
            if word_map.has_key(x):
                word_map[x] -= 1
                if word_map[x] < 0:
                    index_list.pop(index_map[x])
                    self.adjustMap(index_map[x], index_map)
                    word_map[x] = 0
                index_map[x] = len(index_list)
                index_list.append(i)
                if self.isComplete(word_map):
                    if index_list[-1] - index_list[0] < min_dis:
                        min_dis = index_list[-1] - index_list[0]
                        min_start = index_list[0]
                        min_end = index_list[-1]

        if min_start != -1 and min_end != -1:
            return s[min_start:min_end + 1]
        else:
            return ""

    def isComplete(self, word_map):
        num = 0
        for x in word_map.items():
            if x[1] <= 0:
                num += 1
        if num == len(word_map):
            return True
        else:
            return False

    def adjustMap(self, line, my_map):
        for x in my_map.items():
            if x[1] > line:
                my_map[x[0]] -= 1


so = Solution()
# print so.minWindow("ADOBECODEBANC", "ABC")
print so.minWindow("acbbaca", "aba")
