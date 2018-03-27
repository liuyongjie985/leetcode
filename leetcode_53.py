class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]

        i = 0

        row = len(matrix)
        column = len(matrix[0])

        total = row * column

        result = []
        x = 0
        y = 0
        sign = 0
        bias = 0
        result.append(matrix[x][y])
        while i < total - 1:
            x, y, sign, bias = self.nextStep(x, row, y, column, sign, bias)
            result.append(matrix[x][y])
            i += 1
        return result

    def nextStep(self, i, i_max, j, j_max, sign, bias):
        if sign == 0:
            j += 1
            if j >= j_max - bias:
                i += 1
                j = j_max - bias - 1
                sign = 1
            return i, j, sign, bias
        if sign == 1:
            i += 1
            if i >= i_max - bias:
                i = i_max - bias - 1
                j -= 1
                sign = 2
            return i, j, sign, bias
        if sign == 2:
            j -= 1
            if j < 0 + bias:
                j = 0 + bias
                i -= 1
                sign = 3
            return i, j, sign, bias
        if sign == 3:
            i -= 1
            if i < 0 + bias + 1:
                i = bias + 1
                j += 1
                sign = 0
                bias += 1
            return i, j, sign, bias


so = Solution()
print so.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
