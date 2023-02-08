#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @param k int整型
# @return int整型
#
class Solution:
    def GetNumberOfK(self, data: List[int], k: int) -> int:
        # write code here
        if len(data) == 0:
            return 0
        l = 0
        r = len(data) - 1
        while l <= r:
            mid = (l + r) // 2
            if data[mid] < k:
                l = mid + 1
            else:
                r = mid - 1

        down = l

        l = 0
        r = len(data) - 1
        while l <= r:
            mid = (l + r) // 2
            if data[mid] <= k:
                l = mid + 1
            else:
                r = mid - 1
        up = l
        if up > down:
            return up - down
        else:
            return 0
