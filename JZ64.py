#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def __init__(self):
        self.res = 0

    def Sum_Solution(self, n: int) -> int:
        # write code here
        self.stack(n)
        return self.res

    def stack(self, x):
        n = x > 1 and self.stack(x - 1)
        self.res += x


so = Solution()
print(so.Sum_Solution(4))
