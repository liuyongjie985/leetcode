# coding:utf-8
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) <= 0:
            return []
        if len(words) <= 0:
            return []
        words_2_num = {}

        result = []

        for x in words:
            if words_2_num.has_key(x):
                words_2_num[x] += 1
            else:
                words_2_num[x] = 1

        for i, x in enumerate(words[0]):
            now_map = {}
            count = 0
            left = i
            j = i
            while j < len(s):
                now_str = s[j:j + len(words[0])]
                # 如果不在words中就重来
                if words_2_num.has_key(now_str):
                    # 先把单词加进去
                    if now_map.has_key(now_str):
                        now_map[now_str] += 1
                    else:
                        now_map[now_str] = 1

                    if now_map[now_str] <= words_2_num[now_str]:
                        count += 1
                    # 如果同一个字符超了
                    else:

                        while now_map[now_str] > words_2_num[now_str]:

                            temp = s[left:left + len(words[0])];
                            if now_map.has_key(temp):

                                now_map[temp] -= 1
                                if now_map[temp] < words_2_num[temp]:
                                    count -= 1

                            left += len(words[0]);

                    if count == len(words):

                        result.append(left);

                        temp = s[left:left + len(words[0])]
                        if (now_map.has_key(temp)):
                            now_map[temp] -= 1
                        count -= 1;
                        left += len(words[0])



                else:
                    now_map = {}
                    count = 0
                    left = j + len(words[0])
                j += len(words[0])

        return result


so = Solution()

print so.findSubstring(

    "wordgoodgoodgoodbestword",
    ["word", "good", "best", "good"]

)

print so.findSubstring(
    "barfoothefoobarman",
    ["foo", "bar"])

print so.findSubstring(
    "barfoofoobarthefoobarman",
    ["bar", "foo", "the"])

print so.findSubstring(
    "abababab",
    ["a", "b", "a"])

print so.findSubstring("sheateateseatea",
                       ["sea", "tea", "ate"])

print so.findSubstring(
    "aaabbbc",
    ["a", "a", "b", "b", "c"])
