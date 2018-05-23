class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        matrix = []
        for x in xrange(m + 1):
            temp = []
            for y in xrange(n + 1):
                temp.append(-1)
            matrix.append(temp)

        row_map = {}

        for index1 in xrange(m + 1):
            if index1 == 0:
                row_map[index1] = ""
            else:
                row_map[index1] = word1[index1 - 1]
        column_map = {}

        for index2 in xrange(n + 1):
            if index2 == 0:
                column_map[index2] = ""
            else:
                column_map[index2] = word2[index2 - 1]

        for index1, x in enumerate(matrix):
            for index2, y in enumerate(x):
                if index1 == 0:
                    matrix[index1][index2] = index2
                    continue

                if index2 == 0:
                    matrix[index1][index2] = index1
                    continue
                left = matrix[index1][index2 - 1] + 1
                right = matrix[index1 - 1][index2] + 1
                bias = 0 if row_map[index1] == column_map[index2] else 1
                mid = matrix[index1 - 1][index2 - 1] + bias

                matrix[index1][index2] = min(min(left, right), mid)
        return matrix[-1][-1]


so = Solution()
print so.minDistance("horse", "ros")
