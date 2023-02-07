#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num1 int整型
# @param num2 int整型
# @return int整型
#
class Solution:
    def Add(self, num1: int, num2: int) -> int:
        # write code here
        base = (num1 ^ num2) & (2 ** 64 - 1)
        jinwei = num1 & num2 & (2 ** 64 - 1)
        while jinwei != 0:
            num2 = jinwei << 1 & (2 ** 64 - 1)
            num1 = base
            base = (num1 ^ num2) & (2 ** 64 - 1)
            jinwei = num1 & num2 & (2 ** 64 - 1)
        return base if base >> 63 == 0 else base - 2 ** 64


so = Solution()
print(so.Add(-2, -3))
