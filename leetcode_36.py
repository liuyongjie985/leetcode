# coding:utf-8
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) == 0:
            return False

        right3_1 = dict()
        right3_2 = dict()
        right3_3 = dict()
        column_length = 0
        i = 0
        # 每一行
        for x in board:

            if i % 3 == 0:
                right3_1 = dict()
                right3_2 = dict()
                right3_3 = dict()
            if len(x) == 0:
                return False
            else:
                column_length = len(x)
            right = dict()  # 用于检验每个小方格里的数是不是符合规则
            j = 0
            for y in x:
                if 0 <= j and j < 3:
                    if right3_1.has_key(y):
                        return False
                    else:
                        if y != '.':
                            right3_1[y] = 1
                if 3 <= j and j < 6:
                    if right3_2.has_key(y):
                        return False
                    else:
                        if y != '.':
                            right3_2[y] = 1
                if 6 <= j and j < 9:
                    if right3_3.has_key(y):
                        return False
                    else:
                        if y != '.':
                            right3_3[y] = 1
                if right.has_key(y):
                    return False
                else:
                    if y != '.':
                        right[y] = 1

                j += 1

            i += 1

        # 每一列

        for x in xrange(column_length):
            right = dict()
            for y in board:
                if right.has_key(y[x]):
                    return False
                else:
                    if y[x] != '.':
                        right[y[x]] = 1

        return True


so = Solution()
# print so.isValidSudoku([[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
#                         ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
#                         ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
#                         ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
#                         ["9", ".", ".", ".", ".", ".", ".", ".", "."]])





# print so.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."],
#                         [".", ".", ".", ".", ".", ".", ".", ".", "."],
#                         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
#                         [".", ".", ".", "5", "6", ".", ".", ".", "."],
#                         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
#                         [".", ".", ".", "7", ".", ".", ".", ".", "."],
#                         [".", ".", ".", "5", ".", ".", ".", ".", "."],
#                         [".", ".", ".", ".", ".", ".", ".", ".", "."],
#                         [".", ".", ".", ".", ".", ".", ".", ".", "."]])

print so.isValidSudoku([[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
                        ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
                        ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
                        ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                        ["9", ".", ".", ".", ".", ".", ".", ".", "."]])
