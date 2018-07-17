# coding:utf-8
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        matrix = self.createMatrix(s1, s2)

        return matrix[len(s1)][0][0]

    def createMatrix(self, s1, s2):
        matrix = []
        row = []
        # 长度为0的都为True
        for x in s1:
            temp = []
            for y in s2:
                temp.append(True)
            row.append(temp)
        matrix.append(row)

        for length, x in enumerate(s1):
            length = length + 1

            if length == 3:
                print "ok"
            row = []
            for i, y in enumerate(s1):
                if i + length > len(s1):
                    temp = [False, False, False, False, False]
                    row.append(temp)
                    continue
                temp = []
                for j, z in enumerate(s2):

                    if j + length > len(s1):
                        temp.append(False)
                        continue
                    if length == 1:
                        if s1[i] == s2[j]:
                            temp.append(True)
                        else:
                            temp.append(False)
                    else:
                        sign = 0
                        for now_length in xrange(length):
                            if now_length == 0:
                                continue

                            if (matrix[now_length][i][j] == True and
                                matrix[length - now_length][i + now_length][j + now_length]) or (
                                    matrix[now_length][i][j + length - now_length] == True and
                                    matrix[length - now_length][i + now_length][j]):
                                sign = 1
                                break;
                        if sign == 0:
                            temp.append(False)
                        else:
                            temp.append(True)
                row.append(temp)

            matrix.append(row)
        # for x in matrix:
        #     print x
        return matrix


so = Solution()
print so.isScramble("rgtae", "great")
