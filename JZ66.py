#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A int整型一维数组
# @return int整型一维数组
#
class Solution:
    def multiply(self, A):
        # write code here
        B = [1 for x in range(len(A))]

        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        for i in range(len(A))[::-1]:
            B[i] *= temp
            temp *= A[i]

        return B


so = Solution()
print(so.multiply([1, 2, 3, 4, 5]))
