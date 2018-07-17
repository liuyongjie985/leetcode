# coding:utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, left, right, nums, target):
        length = right - left + 1
        if length < 1:
            return False
        if length == 1:
            if nums[left] == target:
                return True
            else:
                return False

        mid = length / 2 + left
        min = nums[left]
        max = nums[right]

        if nums[mid] == target:
            return True
        # 左边有序
        if min < nums[mid]:
            if min <= target and target <= nums[mid]:
                return self.binarySearch(left, mid - 1, nums, target)
            else:
                return self.binarySearch(mid + 1, right, nums, target)
        else:
            # 无法判断哪边有序的时候
            if min == nums[mid]:
                i = 0
                while mid - i >= left and min == nums[mid - i]:
                    i += 1
                if mid - i < left:
                    return self.binarySearch(mid + 1, right, nums, target)
                else:

                    return self.binarySearch(left, mid - 1, nums, target)


            else:
                if target >= nums[mid] and target <= max:
                    return self.binarySearch(mid + 1, right, nums, target)
                else:
                    return self.binarySearch(left, mid - 1, nums, target)


so = Solution()
# print so.search([2, 5, 6, 0, 0, 1, 2], 0)
# print so.search([2, 5, 6, 0, 0, 1, 2], 3)
# print so.search([1, 1, 1, 1, 3], 0)


print so.search([3, 0, 0, 2, 2, 2, 3], 3)
