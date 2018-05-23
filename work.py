# coding:utf-8
class Solution(object):
    def findPosition(self, matrix):
        """
        :type matrix: List[list]
        :rtype: （i,j）
        """

        if len(matrix) < 1:
            return -1, -1
        if len(matrix[0]) < 1:
            return -1, -1

        max = 0
        max_i = -1
        max_j = -1

        for i, x in enumerate(matrix):
            for j, y in enumerate(x):
                if y == 0:
                    continue
                temp = self.calNum(i, len(x), j, len(matrix), matrix)
                if temp > max:
                    max = temp
                    max_i = i
                    max_j = j
        return (max_i, max_j)

    def calNum(self, i, i_max, j, j_max, matrix):

        column_top = 0
        column_bottom = 0
        x = i

        while x >= 0:
            if matrix[x][j] == 0:
                break;
            column_top += 1
            x -= 1
        x = i
        # 需要保证matrix至少长度为1
        while x < j_max:
            if matrix[x][j] == 0:
                break;
            column_bottom += 1

            x += 1

        row_left = 0
        x = j
        while x >= 0:
            if matrix[i][x] == 0:
                break;
            row_left += 1

            x -= 1

        x = j
        row_right = 0
        while x < i_max:
            if matrix[i][x] == 0:
                break;
            row_right += 1

            x += 1
        return column_bottom + column_top + row_left + row_right - 3


so = Solution()
print so.findPosition(
    [[1, 1, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0],
     [1, 1, 0, 1, 1, 0, 1]])
