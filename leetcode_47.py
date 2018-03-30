class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        my_map = {}
        new_list = []
        for x in nums:
            if my_map.has_key(x):
                my_map[x] += 1
            else:
                my_map[x] = 1
                new_list.append(x)

        divide = 1
        for x in my_map.keys():
            if my_map[x] > 1:
                divide *= self.factorial(my_map[x])

        result = self.permute(nums, divide)

        return result

    def permute(self, nums, divided):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]

        length = 2
        kasu = 0

        result = list()
        total = self.factorial(len(nums))
        while kasu < total / divided:

            while length <= len(nums) and kasu < total / divided:
                suffix_nums = nums[len(nums) - length:]
                prefix_nums = nums[:len(nums) - length]

                next_list = self.findNextList(suffix_nums)
                if next_list == []:
                    length += 1
                    continue
                else:
                    result.append(list(prefix_nums + next_list))

                    nums = result[-1]
                    kasu += 1
                    length = 2
            length = 2
            last = list(nums)

            last.reverse()
            result.append(last)
            kasu += 1
            while length <= len(last) and kasu < total / divided:
                suffix_nums = last[len(last) - length:]
                prefix_nums = last[:len(last) - length]

                next_list = self.findNextList(suffix_nums)
                if next_list == []:
                    length += 1
                    continue
                else:
                    result.append(list(prefix_nums + next_list))

                    last = result[-1]
                    kasu += 1
                    length = 2
        print len(result)
        return result

    def findNextList(self, sub_nums):
        i = len(sub_nums) - 1
        while i > 0:

            j = i - 1
            while j >= 0:

                if sub_nums[j] < sub_nums[i]:
                    temp = sub_nums[i]
                    sub_nums[i] = sub_nums[j]
                    sub_nums[j] = temp
                    temp = sub_nums[j + 1:]
                    temp.reverse()

                    return sub_nums[:j + 1] + temp
                j -= 1
            i -= 1

        return []

    def factorial(self, n):
        result = 1
        for x in xrange(n):
            result *= (x + 1)
        return result


so = Solution()
print so.permuteUnique([1, 1, 2])
