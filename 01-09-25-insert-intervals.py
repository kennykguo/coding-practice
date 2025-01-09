class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Labels
        new_start = newInterval[0]
        new_end = newInterval[1]
        # Return list
        res = []

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if new_end < start: # Interval completely before
                res.append([new_start, new_end])
                res += intervals[i:]
                return res

            elif new_start > end: # Completely after, just add the current interval and continue on
                res.append(intervals[i])

            # Merge the interval
            else:
                new_start = min(intervals[i][0], new_start)
                new_end = max(intervals[i][1], new_end)
        res.append([new_start, new_end])
        return res


            