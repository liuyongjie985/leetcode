#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, array):

        # write code here
        su = 0
        for x in array:
            su = su ^ x

        b_su = self.Binary(su)
        target_i = -1
        for i, x in enumerate(b_su):
            if x == "1":
                target_i = i
                break
        array_0 = []
        array_1 = []
        for x in array:
            b_x = self.Binary(x)
            if b_x[target_i] == "0":
                array_0.append(x)
            else:
                array_1.append(x)

        a = 0
        b = 0
        for x in array_0:
            a ^= x

        for x in array_1:
            b ^= x

        if a >= b:
            return [b, a]
        else:
            return [a, b]

    def Binary(self, i):
        result = ""
        while i != 0:
            temp = i % 2
            i = i // 2
            result += str(temp)

        for x in range(64 - len(result)):
            result += "0"

        return result[::-1]


so = Solution()
print(so.FindNumsAppearOnce([1, 2, 3, 3, 2, 9]))
