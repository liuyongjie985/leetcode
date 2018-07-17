class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        index = 0
        available_matrix = self.initAvailable(board)
        for i, x in enumerate(board):
            for j, y in enumerate(x):

                if self.isTure(i, len(board), j, len(board[0]), board, available_matrix, index, word) == True:
                    return True
        return False

    def isTure(self, i, i_max, j, j_max, board, available_matrix, index, word):
        if index >= len(word):
            return True
        if i < 0 or i >= i_max:
            return False
        if j < 0 or j >= j_max:
            return False

        if word[index] == board[i][j] and available_matrix[i][j] != 1:
            available_matrix[i][j] = 1
            index += 1
            if self.isTure(i + 1, i_max, j, j_max, board, available_matrix, index, word) == True:
                return True
            if self.isTure(i, i_max, j + 1, j_max, board, available_matrix, index, word) == True:
                return True
            if self.isTure(i - 1, i_max, j, j_max, board, available_matrix, index, word) == True:
                return True
            if self.isTure(i, i_max, j - 1, j_max, board, available_matrix, index, word) == True:
                return True
            available_matrix[i][j] = 0
            index -= 1
        return False

    def initAvailable(self, board):
        available_matrix = []
        for i, x in enumerate(board):
            temp = []
            for j, y in enumerate(x):
                temp.append(0)
            available_matrix.append(temp)
        return available_matrix


so = Solution()
print so.exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'ABCCED')

print so.exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'SEE')

print so.exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], 'ABCB')
