# coding:utf-8

class Solution(object):

    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        matrix = []

        for x in xrange(n):
            temp = ""
            for y in xrange(n):
                temp += "."
            matrix.append(temp)

        result = list()

        self.toSolve(n, matrix, 0, 0, result)

        return result

    def toSolve(self, n, matrix, i, j, result):
        if i >= n:
            temp = list(matrix)
            result.append(temp)
            return

        while j < n:
            prefix = matrix[i][:j]
            suffix = matrix[i][j + 1:]
            matrix[i] = prefix + "Q" + suffix
            if self.isValid(matrix, i, j):
                self.toSolve(n, matrix, i + 1, 0, result)

            matrix[i] = prefix + "." + suffix

            j += 1

        return result

    def isValid(self, matrix, i, j):
        num = 0
        n = len(matrix)
        for x in matrix:
            if x[j] == 'Q':
                num += 1
                if num == 2:
                    return False

        # 判断左斜列有没有
        x = 1

        while i - x >= 0 and j - x >= 0:
            if matrix[i - x][j - x] == 'Q':
                return False

            x += 1
        # 判断右斜列有没有
        x = 1

        while i - x >= 0 and j + x < n:
            if matrix[i - x][j + x] == 'Q':
                return False

            x += 1
        return True


try:
    so = Solution()
    print so.solveNQueens(4)
except:
    pass


# print so.isValid([".Q..", "Q...", "....", "...."], 1, 0)
