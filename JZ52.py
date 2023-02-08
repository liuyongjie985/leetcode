#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @return int整型
#
class Solution:
    def InversePairs(self, data) -> int:
        # write code here
        sorted_l, r = self.mergesort(data)
        return r % 1000000007

    def mergesort(self, l):
        if len(l) <= 1:
            return l, 0
        else:
            mid = len(l) // 2
            left = l[:mid]
            right = l[mid:]
            s_left, l_num = self.mergesort(left)
            s_right, r_num = self.mergesort(right)
            result = []
            c = 0
            index_l = len(left) - 1
            index_r = len(right) - 1
            while index_l >= 0 and index_r >= 0:
                if s_left[index_l] > s_right[index_r]:
                    result.append(s_left[index_l])
                    c += index_r + 1
                    index_l -= 1

                else:
                    result.append(s_right[index_r])
                    index_r -= 1

            if index_l == -1:
                return s_right[:index_r + 1] + result[::-1], l_num + r_num + c
            else:
                return s_left[:index_l + 1] + result[::-1], l_num + r_num + c


so = Solution()
print(so.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))

# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 2 3
# 2 4
# 5 6
# 2 4
# 2 6
# 4 6
