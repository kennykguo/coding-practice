class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        start = intervals[0][0]
        end = intervals[0][1]
        res = []

        # 1 to len()
        for i in range (1, len(intervals)):
            # New start is less than current end
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
                print("hello")
                if len(intervals) == 2:
                    res.append([start, end])
            else:
                print("hello2")
                print(i)
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        return res
