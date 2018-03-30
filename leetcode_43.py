# coding:utf-8

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = "0"
        i = len(num2) - 1
        while i >= 0:

            temp = self.calculate_row(num1, num2[i])
            for y in xrange(len(num2) - 1 - i):
                temp = temp + "0"
            result = self.add(result, temp)

            i -= 1

        while result[0] == '0' and len(result)>1:
            result = result[1:]

        return result

    def add(self, num1, num2):
        if len(num1) < len(num2):
            for x in xrange(len(num2) - len(num1)):
                num1 = "0" + num1
        else:
            for x in xrange(len(num1) - len(num2)):
                num2 = "0" + num2

        i = len(num1) - 1

        extra = 0
        result = ""
        while i >= 0:
            temp = int(num1[i]) + int(num2[i]) + extra
            extra = temp / 10
            last = temp % 10
            result = str(last) + result

            i -= 1

        if extra != 0:
            result = str(extra) + result

        return result

    # 第一个数是长数，第二个数是数字
    def calculate_row(self, str1, str2):
        length = len(str1) - 1
        result = ""
        extra = 0

        while length >= 0:
            num1 = int(str1[length])
            num2 = int(str2[0])

            temp = num1 * num2 + extra

            extra = temp / 10
            save2 = temp % 10

            result = str(save2) + result

            length -= 1

        if extra != 0:
            result = str(extra) + result

        return result


so = Solution()
# print so.multiply("946", "513")
print so.multiply("946", "0")