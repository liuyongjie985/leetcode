#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @param m int整型
# @return int整型
#
class Solution:
    def LastRemaining_Solution(self, n: int, m: int) -> int:
        # write code here
        a = 1
        res = 1
        while a < n:
            res = (res + (m % (a + 1))) % (a + 1)
            if res == 0:
                res = a + 1
            a += 1
        return res - 1


so = Solution()
print(so.LastRemaining_Solution(10, 17))
