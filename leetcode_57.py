class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return [newInterval]

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

        if start != -1 and start < end:
            pre = sorted_intervals[:start]
            suffix = sorted_intervals[end + 1:]
            temp = Interval()
            temp.start = min(sorted_intervals[start].start, newInterval.start)
            temp.end = max(sorted_intervals[end].end, newInterval.end)
            return pre + [temp] + suffix
        else:
            if start == end:
                pre = sorted_intervals[:start]
                suffix = sorted_intervals[start + 1:]
                temp = [min(sorted_intervals[start].start, newInterval.start),
                        max(sorted_intervals[start].end, newInterval.end)]
                return pre + [temp] + suffix
            if start != -1 and end == -1:
                # 放在列表第一个

                return [newInterval] + sorted_intervals
            else:
                if start == -1 and end == -1:
                    # 放在列表最后一个
                    pre = sorted_intervals[:len(sorted_intervals) - 1]
                    return pre + [newInterval]
                else:
                    if start - 1 == end:
                        pre = sorted_intervals[:end + 1]
                        suffix = sorted_intervals[end + 1:]
                        return pre + [newInterval] + suffix
                    else:
                        if start == -1 and end != -1:
                            # 放在列表最后一个
                            return sorted_intervals + [newInterval]

                        return sorted_intervals

    def quickSort(self, intervals):
        if len(intervals) <= 1:
            return intervals
        mid = intervals[len(intervals) / 2]

        left_list = [x for x in intervals if x.start < mid.start]
        mid_list = [x for x in intervals if x.start == mid.start]
        right_list = [x for x in intervals if x.start > mid.start]

        return self.quickSort(left_list) + mid_list + self.quickSort(right_list)