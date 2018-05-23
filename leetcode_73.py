class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        index_list = []
        for index1, x in enumerate(matrix):
            for index2, y in enumerate(x):
                if y == 0:
                    index_list.append((index1, index2))

        for x in index_list:
            self.oneSetZero(x[0], x[1], matrix)

    def oneSetZero(self, i, j, matrix):
        i_new = 0
        while i_new < len(matrix):
            matrix[i_new][j] = 0
            i_new += 1
        j_new = 0
        while j_new < len(matrix[i]):
            matrix[i][j_new] = 0
            j_new += 1
        return matrix


so = Solution()
m = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
so.setZeroes(m)
print m
