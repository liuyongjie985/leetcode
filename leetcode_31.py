class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        sorted = list(nums)

        sorted.sort()

        index = 0
        for x in xrange(len(nums)):
            if x == len(nums) - 1:
                continue
            if nums[len(nums) - 2 - x] < nums[len(nums) - 1 - x]:
                index = len(nums) - 2 - x
                break;

        sub_nums = nums[index:]
        pre_nums = nums[:index]

        suffix_nums = self.adjustSubstring(sub_nums)

        while len(suffix_nums) == 0 and index > 0:
            index -= 1
            sub_nums = nums[index:]
            pre_nums = nums[:index]
            suffix_nums = self.adjustSubstring(sub_nums)

        if len(suffix_nums) == 0:
            i = 0
            for p in sorted:
                nums[i] = p
                i += 1
                # return sorted

        else:
            i = 0
            for p in pre_nums + suffix_nums:
                nums[i] = p
                i += 1
                # return pre_nums + suffix_nums

    def adjustSubstring(self, sub_nums):
        end = len(sub_nums)

        re = []
        sign = 0
        for x in xrange(end - 1):
            now = end - 1 - x
            move = end - 1 - x
            while move > 0:
                if sub_nums[move - 1] < sub_nums[now]:
                    temp = sub_nums[move - 1]
                    sub_nums[move - 1] = sub_nums[now]
                    sub_nums[now] = temp

                    new_nums = list(sub_nums[move:])
                    new_nums.reverse()
                    for y in xrange(move):
                        re.append(sub_nums[y])
                    re = re + new_nums

                    sign = 1
                    break;
                move -= 1

            if sign == 1:
                break;
        return re


so = Solution()
nums = [4, 2, 0, 2, 3, 2, 0]
so.nextPermutation(nums)
print nums
# print so.nextPermutation([2, 1, 3])
# print so.nextPermutation([3, 2, 1])
# print so.nextPermutation([1, 2, 5, 4, 3])
