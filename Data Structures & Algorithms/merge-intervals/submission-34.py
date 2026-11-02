class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                
        intervals.sort(key = lambda x: x[0])

        # print(intervals)

        # our intervals are sorted, check them one by one
        res = []
        res.append(intervals[0])
        cur_max = intervals[0][1]
        for interval in range(1, len(intervals), 1):
            [i,j] = intervals[interval]
            if i <= cur_max: # overlapping
                res[-1][1] = max(res[-1][-1], j) # last element of stack, might need to change it's end interval. take the max of that and the new interval
                cur_max = res[-1][1]
            else: # non overlapping
                print(i,j)
                res.append([i,j])
                cur_max = res[-1][1]

        # print(res)
        return res