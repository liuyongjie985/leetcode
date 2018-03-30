# coding:utf-8

# ‘bar’ | ‘foo’ | ‘the’ | ‘foo’ | ‘bar’ | ‘man’
# ‘arf’ | ‘oot’ | ‘hef’ | ‘oob’ | ‘arm’
# ‘rfo’ | ‘oth’ | ‘efo’ | ‘oba’ | ‘rma’

# s: "barfoothefoobarman"
# words: ["foo", "bar"]

class Solution(object):
    def getWord(self, step, index, s):

        try:
            return index + step, s[index:index + step]
        except:
            return 0, ""

    def doAIteration(self, index, step, s, words_map, b, e):
        l = len(s)
        start = index
        total = 0
        temp = dict()
        # index_map = dict()

        while index < l:
            index, word = self.getWord(step, index, s)
            if word != "":
                if words_map.has_key(word):
                    # 加入temp
                    if temp.has_key(word):

                        temp[word] = temp[word] + 1
                        total += 1
                        if temp[word] > words_map[word]:

                            temp[word] -= 1
                            total -= 1

                            if temp == words_map:
                                start += step
                                b.append(start)
                                e.append(index)

                            start = self.findIndex(temp[word], word, s[:index], step)
                            self.getNewWord(s[start:index], temp, step)






                    else:
                        temp[word] = 1
                        total += 1

                    if temp == words_map:
                        b.append(start)
                        e.append(index)
                        temp[s[start:start + step]] -= 1
                        total -= 1
                        start += step

                        # if temp[word] == words_map[word] - 1:
                        #     index_map[word] = index



                else:
                    start = index
                    temp.clear()



            else:
                break;

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if s == "" or len(words) == 0:
            return []

        words_map = dict()
        num = 0
        # 先把words转化成map
        for x in words:
            if words_map.has_key(x):
                words_map[x] = words_map[x] + 1
            else:
                words_map[x] = 1
            num += 1

        b = []
        e = []
        num_iteration = len(words[0])

        for x in xrange(num_iteration):
            self.doAIteration(x, num_iteration, s, words_map, b, e)

        return b

    def findIndex(self, target_num, target_word, s, step):
        end = len(s)
        temp = dict()
        temp[target_word] = 0
        while end >= 0 + step:
            word = s[end - step:end]
            if temp.has_key(word):
                temp[word] += 1
            else:
                temp[word] = 1

            if temp[target_word] > target_num:
                return end

            end -= step

    def getNewWord(self, s, my_map, step):
        my_map.clear()
        start = 0
        while start < len(s):
            word = s[start:start + step]
            if my_map.has_key(word):
                my_map[word] += 1
            else:
                my_map[word] = 1
            start += step


so = Solution()
# print so.findSubstring(
#
#     "wordgoodgoodgoodbestword",
#     ["word", "good", "best", "good"]
#
# )

# print so.findSubstring(
#     "barfoothefoobarman",
#     ["foo", "bar"])





# print so.findSubstring(
#     "barfoofoobarthefoobarman",
#     ["bar", "foo", "the"])

# print so.findSubstring(
#     "abababab",
#     ["a", "b", "a"])


# print so.findSubstring("sheateateseatea",
#                       ["sea", "tea", "ate"])

#
# print so.findSubstring(
#     "aaabbbc",
#     ["a", "a", "b", "b", "c"])
