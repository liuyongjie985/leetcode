# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 1:
            return intervals

        sorted_intervals = self.quickSort(intervals)

        i = 1
        while i < len(sorted_intervals):
            if sorted_intervals[i].start <= sorted_intervals[i - 1].end:
                start = sorted_intervals[i - 1].start
                end = max(sorted_intervals[i].end, sorted_intervals[i - 1].end)
                temp = Interval()
                temp.start = start
                temp.end = end
                sorted_intervals.pop(i - 1)
                sorted_intervals.pop(i - 1)
                sorted_intervals.insert(i - 1, temp)
            else:
                i += 1
        return sorted_intervals

    def quickSort(self, intervals):
        if len(intervals) <= 1:
            return intervals
        mid = intervals[len(intervals) / 2]

        left_list = [x for x in intervals if x.start < mid.start]
        mid_list = [x for x in intervals if x.start == mid.start]
        right_list = [x for x in intervals if x.start > mid.start]

        return self.quickSort(left_list) + mid_list + self.quickSort(right_list)


so = Solution()
my_list = []

temp = Interval()
temp.start = 1
temp.end = 3

my_list.append(temp)

temp = Interval()
temp.start = 2
temp.end = 6

my_list.append(temp)

temp = Interval()
temp.start = 8
temp.end = 10

my_list.append(temp)

temp = Interval()
temp.start = 15
temp.end = 18

my_list.append(temp)

print so.merge(my_list)
