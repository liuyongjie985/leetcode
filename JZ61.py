#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsContinuous(self, numbers) -> bool:
        # write code here
        min = 20
        max = -1
        d_dict = {}
        zero_num = 0
        for x in numbers:
            if x == 0:
                zero_num += 1
            else:
                if x in d_dict:
                    return False
                else:
                    d_dict[x] = 1
                if min > x:
                    min = x

                if max < x:
                    max = x

        if max - min > 4:
            return False
        else:
            if len(d_dict) + zero_num == 5:
                return True
            else:
                return False


so = Solution()
print(so.IsContinuous([13, 12, 11, 0, 1]))
