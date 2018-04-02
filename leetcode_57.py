# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Example 3:
# Given [1,2],[12,16], insert and merge [4,9] in as [1,2],[4,9],[12,16].

# Example 4:
# Given [1,2],[4,9], insert and merge [12,16] in as [1,2],[4,9],[12,16].


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        sorted_intervals = self.quickSort(intervals)

        start = -1
        end = -1

        i = 0
        for x in sorted_intervals:
            if newInterval.start <= x.end:
                start = i
                break;
            i += 1

        i = 0
        for x in sorted_intervals:
            if x.start <= newInterval.end:
                end = i
            i += 1

        if start < end:
            pre = sorted_intervals[:start]
            suffix = sorted_intervals[end + 1:]

            return pre + [newInterval] + suffix
        else:
            if start != -1 and end != -1:



        end =

    def quickSort(self, intervals):
        if len(intervals) <= 1:
            return intervals
        mid = intervals[len(intervals) / 2]

        left_list = [x for x in intervals if x.start < mid.start]
        mid_list = [x for x in intervals if x.start == mid.start]
        right_list = [x for x in intervals if x.start > mid.start]

        return self.quickSort(left_list) + mid_list + self.quickSort(right_list)


so = Solution()
so
