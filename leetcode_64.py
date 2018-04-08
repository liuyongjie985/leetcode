# coding:utf-8
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = []
        for index1, x in enumerate(grid):
            temp = []
            for index2, y in enumerate(x):
                # 第一个数
                if index1 == 0 and index2 == 0:
                    temp.append(grid[index1][index2])
                    continue
                # 第一行
                if index1 == 0:
                    temp.append(temp[-1] + grid[index1][index2])
                    continue
                # 第一列
                if index2 == 0:
                    temp.append(result[-1][0] + grid[index1][index2])
                    continue

                # 正常
                temp.append(min(temp[-1], result[-1][index2]) + y)
            result.append(temp)
        return result[-1][-1]


so = Solution()
print so.minPathSum([[1, 3, 1],
                     [1, 5, 1],
                     [4, 2, 1]])
