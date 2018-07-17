class Solution(object):
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
# print so.largestRectangleArea([1])
# print so.largestRectangleArea([2, 1, 5, 6, 2, 3])
# print so.largestRectangleArea([2, 1, 2])
print so.largestRectangleArea([2, 1, 5, 6, 2, 3])
# print so.largestRectangleArea([])
