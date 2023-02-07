#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloorII(self, number: int) -> int:
        # write code here
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)
        total = 3
        for x in range(18):
            dp.append(total + 1)
            total += dp[-1]
        return dp[number]
