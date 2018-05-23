class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) <= 0:
            return False
        if len(matrix[0]) <= 0:
            return False
        return self.BinarySearch(0, len(matrix) * len(matrix[0]), matrix, target)

    def translateIndex(self, value, j_max):
        i = value / j_max
        j = value % j_max
        return i, j

    def BinarySearch(self, left, right, matrix, target):
        length = right - left
        if length <= 0:
            return False
        if length == 1:
            i, j = self.translateIndex(left, len(matrix[0]))
            if matrix[i][j] == target:
                return True
            else:
                return False

        mid = left + length / 2

        i, j = self.translateIndex(mid, len(matrix[0]))
        if matrix[i][j] == target:
            return True
        else:
            if matrix[i][j] > target:
                return self.BinarySearch(left, mid, matrix, target)
            else:
                return self.BinarySearch(mid, right, matrix, target)


so = Solution()

print so.searchMatrix([[1], [3]]
                      , 1)

print so.searchMatrix([[1, 3, 5, 7],
                       [10, 11, 16, 20],
                       [23, 30, 34, 50]], 3)

print so.searchMatrix([[1, 3, 5, 7],
                       [10, 11, 16, 20],
                       [23, 30, 34, 50]], 13)
print so.searchMatrix([[1, 3]], 3)
