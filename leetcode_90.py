class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = self.quickSort(nums)

        result = []
        last = None
        last_length = None
        for x in sorted_nums:

            temp_a = []
            temp_b = [x]
            if len(result) == 0:
                result.append(temp_a)
                result.append(temp_b)
                last = x
                last_length = 1
            else:
                new_result = []
                if last == x:
                    total = 0
                    for y in result:
                        new_result.append(y + temp_a)
                    for y in result:
                        if total < last_length:
                            total += 1
                            continue
                        new_result.append(y + temp_b)

                else:

                    for y in result:
                        new_result.append(y + temp_a)
                    for y in result:
                        new_result.append(y + temp_b)
                last_length = len(result)
                last = x
                result = new_result
        return result

    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums

        middle = len(nums) / 2

        left = [x for x in nums if x < nums[middle]]
        mid = [x for x in nums if x == nums[middle]]
        right = [x for x in nums if x > nums[middle]]

        return self.quickSort(left) + mid + self.quickSort(right)


so = Solution()
print so.subsetsWithDup([1, 2, 2, 3, 3])
