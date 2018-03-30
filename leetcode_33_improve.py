# coding:utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        else:
            return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, start, end, target):
        length = end - start + 1
        if length == 1:
            if nums[start] == target:
                return start
            else:
                return -1
        else:
            mid = length / 2 + start
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > nums[end]:
                    # 左边有序
                    min = nums[start]
                    max = nums[mid]
                    if min <= target and target <= max:

                        return self.binarySearch(nums, start, mid, target)
                    else:

                        return self.binarySearch(nums, mid + 1, end, target)
                else:
                    # 右边有序

                    min = nums[mid]
                    max = nums[end]
                    if min <= target and target <= max:

                        return self.binarySearch(nums, mid, end, target)
                    else:

                        return self.binarySearch(nums, start, mid - 1, target)


so = Solution()
# print so.search([0, 1, 2, 4, 5, 6, 7], 0)
#
# print so.search([6, 7, 0, 1, 2, 4, 5], 0)
# print so.search([5, 6, 7, 0, 1, 2, 4], 5)
# print so.search([4, 5, 6, 7, 0, 1, 2], 2)
print so.search([2, 4, 5, 6, 7, 0, 1], 1)
# print so.search([1, 2, 4, 5, 6, 7, 0], 0)
