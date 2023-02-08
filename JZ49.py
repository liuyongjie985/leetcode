#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param index int整型
# @return int整型
#
class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        # write code here
        if index == 0:
            return 0

        dp = [1]
        dp_dict = {}
        index_2 = 0
        index_3 = 0
        index_5 = 0
        while len(dp) < index:
            temp1 = dp[index_2] * 2
            temp2 = dp[index_3] * 3
            temp3 = dp[index_5] * 5
            result = min(temp1, temp2, temp3)

            if result == temp1:
                index_2 += 1
            else:
                if result == temp2:
                    index_3 += 1
                else:
                    index_5 += 1
            if result in dp_dict:
                continue
            else:
                dp_dict[result] = 1
                dp.append(result)
        return dp[-1]

so = Solution()
print(so.GetUglyNumber_Solution(7))