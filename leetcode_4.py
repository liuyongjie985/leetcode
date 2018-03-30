# coding:utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)

        i = 0
        j = 0
        new_list = []
        while i < length1 and j < length2:
            if nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        # 最后需要把剩下的加入列表
        if j == length2:
            new_list = new_list + nums1[i:]
        else:
            new_list = new_list + nums2[j:]

        idx = (len(new_list) - 1) / 2

        if len(new_list) % 2 != 0:
            return round(new_list[idx], 1)
        else:
            return round(float((new_list[idx] + new_list[idx + 1]) / 2.0), 1)


s = Solution()
print s.findMedianSortedArrays([1, 3], [2,4])
