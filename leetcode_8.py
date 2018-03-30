import traceback


class Solution(object):
    def myAtoi(self, mystr):
        """
        :type str: str
        :rtype: int
        """
        if mystr == "":
            return 0
        int_list = ""
        sign = 0
        num = 0
        nowrong = 0
        for x in mystr:
            if num == 1:
                try:
                    temp = int(x)
                    num = 0
                except:
                    return 0

            if (x == " " or x == '\t') and nowrong == 0:
                continue

            if x == "+" or x == "-":
                num = 1
                nowrong = 1
                if x == "-":
                    sign = -1
                continue

            try:
                temp = int(x)
                int_list += str(temp)
                nowrong = 1
            except:
                traceback.print_exc()
                break;

        if len(int_list) == 0:
            return 0

        if sign == 0:
            return int(int_list) if int(int_list) < 2147483648 else 2147483647
        else:
            return 0 - int(int_list) if int(int_list) <= 2147483648 else -2147483648


so = Solution()
print so.myAtoi("  -0012a42")
