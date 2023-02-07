#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def StrToInt(self, s: str) -> int:
        # write code here
        s = self.skipSpace(s)
        if len(s) == 0:
            return 0
        sign = "+"
        if s[0] == "+" or s[0] == "-":
            if s[0] == "-":
                sign = "-"
            s = s[1:]
        res = 0
        t_d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        for x in s:
            if x in t_d:
                res = res * 10 + t_d[x]
            else:
                break

        if sign == "-":
            res = 0 - res
        a = -2 ** 31
        if res < (-2 ** 31):
            res = -2 ** 31
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1

        return res

    def skipSpace(self, s):
        return s.strip()


so = Solution()
print(so.StrToInt("-987654321111"))
