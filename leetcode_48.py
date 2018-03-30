class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)
        if length == 0:
            return [[]]

        self.rotateForOne(matrix, 0)

        return matrix

    def rotateForOne(self, matrix, bias):

        length = len(matrix)

        if length - 2 * bias <= 1:
            return

        # nums = (length - 2 * bias - 1) * 4


        i = bias
        j = bias
        sign = 0
        p = 0
        while p < length - 2 * bias - 1:
            x = 1
            temp_i = i
            temp_j = j
            temp_sign = sign
            to_save = matrix[temp_i][temp_j]

            while x <= 4:

                for y in xrange(length - 2 * bias - 1):
                    temp_i, temp_j, temp_sign = self.clockwiseNext(temp_i, temp_j, length, temp_sign, bias)

                temp = matrix[temp_i][temp_j]
                matrix[temp_i][temp_j] = to_save
                to_save = temp

                x += 1
            j += 1
            p += 1

        self.rotateForOne(matrix, bias + 1)

    def clockwiseNext(self, i, j, length, sign, bias):
        if sign == 0:
            j += 1
            if j >= (length - bias):
                j = length - bias * 2 - 1 + bias
                i = 1 + bias
                sign = 1
            return i, j, sign
        if sign == 1:
            i += 1
            if i >= (length - bias):
                i = length - bias * 2 - 1 + bias
                j = length - bias * 2 - 1 + bias - 1
                sign = 2
            return i, j, sign

        if sign == 2:
            j -= 1
            if j < bias:
                j = bias
                i = length - bias * 2 - 1 + bias - 1
                sign = 3
            return i, j, sign

        if sign == 3:
            i -= 1
            if i < bias:
                i = bias
                j = bias + 1
                sign = 0
            return i, j, sign


so = Solution()
length = 5
i = 1
j = 1
sign = 0
# for x in xrange(4 * length - 3):
#     i, j, sign = so.clockwiseNext(i, j, length, sign, bias=0)
#     print i, j, sign

# for x in xrange(4 * length - 3):
#     i, j, sign = so.clockwiseNext(i, j, length, sign, bias=1)
#     print i, j, sign

# print so.rotate([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ], )

print so.rotate([[5, 1, 9, 11],
                 [2, 4, 8, 10],
                 [13, 3, 6, 7],
                 [15, 14, 12, 16]])
