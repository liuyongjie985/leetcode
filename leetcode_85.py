class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        max = 0
        for i, x in enumerate(matrix):
            temp = self.largestRectangleArea(self.changeToList(matrix[:i + 1]))
            if temp > max:
                max = temp
        return max

    def changeToList(self, matrix):
        my_list = []
        i = 0
        while i < len(matrix[0]):
            j = len(matrix) - 1
            sum = 0
            while j >= 0 and matrix[j][i] != '0':
                sum += 1
                j -= 1
            my_list.append(sum)

            i += 1
        return my_list

    def changeMatrix(self, matrix):
        for x in matrix:
            for i, y in enumerate(x):
                if i == 0:
                    continue
                if x[i - 1] != '0' and x[i] != '0':
                    x[i] = str(int(x[i - 1]) + 1)

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max = 0
        stack = []
        for i, x in enumerate(heights):
            if len(stack) == 0:
                stack.append(x)
                continue
            if stack[-1] <= x:
                stack.append(x)
            else:

                new_list = []

                j = 1
                temp_max = 0
                while len(stack) != 0:
                    top = stack[-1]
                    stack.pop(-1)
                    if temp_max < j * top:
                        temp_max = j * top
                    j += 1
                    if top < x:
                        new_list.append(top)
                    else:
                        new_list.append(x)
                if temp_max > max:
                    max = temp_max

                # for k in xrange(origin_length + 1):
                # stack.append(x)
                new_list.reverse()
                new_list.append(x)
                stack = new_list

        j = 1
        temp_max = 0
        while len(stack) != 0:
            top = stack[-1]
            stack.pop(-1)
            if temp_max < j * top:
                temp_max = j * top
            j += 1

        if temp_max > max:
            max = temp_max
        # for x in xrange(origin_length + 1):
        #     stack.append(x)

        return max


so = Solution()
print so.maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
)
