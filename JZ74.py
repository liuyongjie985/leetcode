#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sum int整型
# @return int整型二维数组
#
class Solution:
    def FindContinuousSequence(self, sum: int):
        # write code here
        n = 2
        result = []
        while True:
            x = sum / n + (1 - n) / 2
            if x <= 0:
                break
            if x == int(x):
                result.append([int(x + p) for p in range(n)])
            n += 1

        return result[::-1]
