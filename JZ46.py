#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self, nums: str) -> int:
        # write code here

        dp = []
        now_str = ""
        for i, x in enumerate(nums):
            if i == 0:
                now_str += x
                if int(now_str) == 0:
                    dp.append(0)
                else:
                    dp.append(1)
            else:
                if i == 1:
                    now_str += x
                    if x == "0":
                        if int(now_str) > 20 or int(now_str) == 0:
                            dp.append(0)
                        else:
                            dp.append(1)
                    else:
                        if now_str[0] == "0":
                            dp.append(0)
                        else:
                            if int(now_str) > 0 and int(now_str) <= 26:
                                dp.append(2)
                            else:
                                dp.append(1)
                    now_str = x
                else:
                    now_str += x
                    result = dp[-1]
                    if x == "0":
                        if int(now_str) > 0 and int(now_str) <= 26:
                            result = dp[-2]
                        else:
                            result = 0
                    else:
                        if int(now_str) > 0 and int(now_str) <= 26 and now_str[0] != "0":
                            result += dp[-2]

                    dp.append(result)
                    now_str = x
        return dp[-1]


so = Solution()
print(so.solve("0"))
