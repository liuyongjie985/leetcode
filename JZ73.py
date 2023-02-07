#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param str string字符串
# @return string字符串
#
class Solution:
    def ReverseSentence(self, str: str) -> str:
        # write code here
        words = []
        word = ""
        i = 0
        space_i = {}
        while i < len(str):
            if str[i] == " ":
                words.append(word)
                word = ""
                while i < len(str) and str[i] == " ":
                    space_i[i] = 1
                    i += 1
                continue
            else:
                word += str[i]
            i += 1
        if word != "":
            words.append(word)

        i = 0
        res = ""
        j = len(words) - 1
        while i < len(str):
            if len(str) - 1 - i in space_i:
                res += " "
                i += 1
                continue
            else:
                res += words[j]
                i += len(words[j])
                j -= 1
        return res


so = Solution()
print(so.ReverseSentence(" nowcoder. a am I "))
