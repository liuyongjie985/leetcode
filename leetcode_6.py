import numpy  as np


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        length = len(s)
        if length == 0:
            return ""
        if numRows == 1:
            return s

        column_num = length / (2 * numRows - 2)
        column_num += 1
        column_num *= (numRows - 1)
        temp_list = []
        for x in xrange(numRows):
            temp = []
            for y in xrange(column_num):
                temp.append('')
            temp_list.append(temp)

        my_matrix = np.mat(temp_list)

        i = 0
        j = 0

        dx = 1
        dy = 0
        for x in xrange(length):
            my_matrix[i, j] = s[x]
            i += dx
            j += dy
            if i >= numRows or i < 0:
                if dy == 0:
                    dy = 1
                    j += 1
                else:
                    j -= 1
                    dy = 0
                if dx > 0:
                    i = numRows - 2
                    dx = -1
                else:
                    i = 1
                    dx = 1

        return ''.join(self.out(my_matrix, numRows, column_num))

    def out(self, my_matrix, row, column):
        list = []
        for x in xrange(row):
            for y in xrange(column):
                if my_matrix[x, y] != '':
                    list.append(my_matrix[x, y])
        return list


so = Solution()
print so.convert("falweiojujwekuimhbkwktjncgbccrzitlgyvxjsgfysbghjjrfumqjpyktddsnxftvdqgxzlvrneaynufhgyqxwaqzelm",
                 48)
