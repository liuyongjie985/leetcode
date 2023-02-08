#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @param sum int整型
# @return int整型一维数组
#
class Solution:
    def FindNumbersWithSum(self, array: List[int], sum: int) -> List[int]:
        # write code here
        d = {}

        for x in array:
            if sum - x in d:
                return [x, sum - x]
            else:
                d[x] = 1

        return []