#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def getGao(self, n):
        s_n = str(n)
        if len(s_n) == 1:
            return n, 0
        else:
            return int(s_n[0]), int(s_n[1:])

    def NumberOf1Between1AndN_Solution(self, n: int) -> int:
        # write code here
        target = 1
        sub_div = 10
        res = 1
        result = 0
        while res != 0:
            res = n // sub_div
            result += res * sub_div // 10
            yu = n % sub_div
            if_gao, if_yu = self.getGao(yu)
            if if_gao == target:
                result += if_yu + 1
            else:
                if if_gao > target:
                    result += sub_div // 10

            sub_div *= 10
        return result
