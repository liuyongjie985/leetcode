class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1, 2], [4, 3]]

        matrix = []
        for x in xrange(n):
            temp = []
            for y in xrange(n):
                temp.append(0)
            matrix.append(temp)

        i = 0
        j = 0
        sign = 0
        bias = 0
        for x in xrange(n * n):
            matrix[i][j] = x + 1
            i, j, sign, bias = self.getNext(matrix, i, j, n, n, sign, bias)
        return matrix

    def getNext(self, matrix, i, j, i_max, j_max, sign, bias):
        if sign == 0:
            j += 1
            if j >= j_max - bias:
                j = j_max - bias - 1
                i += 1
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
            if j < bias:
                j = bias
                i -= 1
                sign = 3
            return i, j, sign, bias

        if sign == 3:
            i -= 1
            if i < bias + 1:
                i = bias + 1
                j += 1
                bias += 1
                sign = 0
            return i, j, sign, bias


so = Solution()
print so.generateMatrix(6)
