class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[0])

        # cur_start = intervals[0][0]
        # cur_end = intervals[0][1]
        res = 0
        # cur = 0

        temp = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] < temp[-1][1]:
                if temp[-1][1] > interval[1]:
                    temp[-1][-1] = interval[0]
                    temp[-1][-1] = interval[1]
                res+= 1
            else:
                temp.append(interval)

        return res