class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        i = len(obstacleGrid)
        if i == 0:
            return 0
        j = len(obstacleGrid[0])

        if j == 0:
            return 0
        if obstacleGrid[i - 1][j - 1] == 1:
            return 0

        return self.returnNum(i - 1, j - 1, obstacleGrid)

    def isOK(self, i, j, obstacleGrid):
        while i >= 0:
            if obstacleGrid[i][j] == 1:
                return False
            i -= 1
        return True

    def isOK2(self, i, j, obstacleGrid):
        while j >= 0:
            if obstacleGrid[i][j] == 1:
                return False
            j -= 1
        return True

    def returnNum(self, i, j, obstacleGrid):
        if j == 0:
            if self.isOK(i, j, obstacleGrid) == True:
                return 1
            else:
                return 0
        if i == 0:
            if self.isOK2(i, j, obstacleGrid) == True:
                return 1
            else:
                return 0
        left = 0
        right = 0
        if obstacleGrid[i][j - 1] == 0:
            left = self.returnNum(i, j - 1, obstacleGrid)
        if obstacleGrid[i - 1][j] == 0:
            right = self.returnNum(i - 1, j, obstacleGrid)

        return left + right


so = Solution()
# print so.uniquePathsWithObstacles([
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ])

print so.uniquePathsWithObstacles([

    [1, 0]

])
