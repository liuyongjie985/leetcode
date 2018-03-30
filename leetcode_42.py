class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        max_index = 0
        max = height[0]
        for i, x in enumerate(height):
            if x > max:
                max = x
                max_index = i
        left_list = height[:max_index + 1]
        right_list = height[max_index:]

        l_result = self.find(left_list)
        r_result = self.find(right_list[::-1])

        return l_result + r_result

    def find(self, left_list):

        l = len(left_list)

        index2 = -1
        num2 = 1

        result = 0

        num1, index1 = self.findFirstGreat(left_list, 1)

        while index1 < l - 1:
            # left_list = left_list[index2 + 1:]

            # num1, index1 = self.findFirstGreat(left_list, num2)

            last = left_list[index1 + 1:]

            num2, index2 = self.findFirstGreat(last, num1)

            height = num1 if num1 < num2 else num2

            length = index2

            total = height * length

            last = left_list[index1 + 1:index2 + index1 + 1]

            subtractor = 0

            for x in last:
                if x < height:
                    subtractor += x
            result += total - subtractor

            index1 = index2 + index1 + 1
            num1 = num2
        return result

    def findFirstGreat(self, my_list, target):
        for i, x in enumerate(my_list):
            if x >= target:
                return x, i
        return 0, len(my_list)


so = Solution()
print so.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
