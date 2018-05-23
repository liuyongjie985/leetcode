# coding:utf-8
class Solution(object):

    def noSpace(self, l):
        temp = []
        for x in l:
            if x != "":
                temp.append(x)
        return temp

    def dealLast(self, l, maxWidth):

        result = ""
        i = 0
        while i < len(l[-1]):
            if l[-1][i] == ' ':
                temp = ""
                start = i

                while i < len(l[-1]) and l[-1][i] == ' ':
                    i += 1
                temp = l[-1][:start] + " " + l[-1][i:]

                result += " "
            else:
                result += l[-1][i]
                i += 1

        while len(result) < maxWidth:
            result += " "
        return result

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # if len(words) == 0:
        #     return []
        #
        # words = self.noSpace(words)
        #
        # if len(words) == 0:
        #     return [""]

        i = 0
        length = 0
        result = []
        temp = []

        while i < len(words):

            if length + len(words[i]) >= maxWidth:
                if length + len(words[i]) == maxWidth:
                    temp_str = ""
                    for x in temp:
                        temp_str += x
                        temp_str += " "
                    temp_str += words[i]

                    temp = []
                    length = 0
                    result.append(temp_str)
                # 如果不是正好包含这个词，那么这个词就不要加入
                else:
                    temp, length = self.saveNoOne(length, maxWidth, temp, result, words[i])

            else:

                length += len(words[i])
                length += 1
                temp.append(words[i])
            i += 1

        if len(temp) != 0:
            temp, length = self.saveNoOne(length, maxWidth, temp, result, "")

        ok = self.dealLast(result, maxWidth)
        result.pop(-1)
        result.append(ok)
        return result

    def saveNoOne(self, length, maxWidth, temp, result, word):
        temp_str = ""
        last = maxWidth - length + len(temp)

        if len(temp) == 1:
            space = ""
            for x in xrange(last):
                space += " "
            result.append(temp[0] + space)
            temp = [word]
            length = len(word) + 1
            return temp, length

        av = last / (len(temp) - 1)
        bias = last % (len(temp) - 1)

        hutsu = ""

        for x in xrange(av):
            hutsu += " "

        special = hutsu + " "

        for index, x in enumerate(temp):
            if index == len(temp) - 1:
                continue
            temp_str += x

            if index < bias:
                temp_str += special
            else:
                temp_str += hutsu

        temp_str += temp[-1]

        result.append(temp_str)
        temp = [word]
        length = len(word) + 1

        return temp, length


def my_print(l):
    for x in l:
        print x


so = Solution()

my_print(so.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
# my_print(so.fullJustify([""], 2))


["This    is    an","example  of text","justification.   "]