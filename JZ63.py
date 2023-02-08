#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices) -> int:
        # write code here
        minprice = 10001
        res = 0
        for x in prices:
            if x < minprice:
                minprice = x
            temp = x - minprice
            if temp > res:
                res = temp
        return res


so = Solution()
print(so.maxProfit([3,2,1]))
