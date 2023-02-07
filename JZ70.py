#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def rectCover(self, number: int) -> int:
        # write code
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)
        for x in range(40):
            dp.append(dp[-1] + dp[-2])
        return dp[number]
