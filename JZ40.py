#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self, input, k):
        # write code here
        if k > len(input) or k == 0:
            return []
        else:
            return self.quicksort(0, len(input) - 1, input, k)

    def quicksort(self, start, end, t_list, k):
        if start > end:
            return t_list
        else:
            medium = self.partition(start, end, t_list)
            if medium == k:
                return t_list[:k]
            else:
                if medium < k:
                    return self.quicksort(medium + 1, end, t_list, k)
                else:
                    return self.quicksort(start, medium - 1, t_list, k)

    def partition(self, start, end, t_list):
        origin_start = start
        start += 1
        while start <= end:
            if t_list[start] > t_list[origin_start]:
                temp = t_list[end]
                t_list[end] = t_list[start]
                t_list[start] = temp
                end -= 1
            else:
                start += 1
        temp = t_list[start - 1]
        t_list[start - 1] = t_list[origin_start]
        t_list[origin_start] = temp
        return start - 1


so = Solution()
print(so.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 8))
