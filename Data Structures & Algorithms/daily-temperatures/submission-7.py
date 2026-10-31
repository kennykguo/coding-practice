class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        length = len(temperatures)

        for i in range(length - 1, -1, -1):
            temp = temperatures[i]

            # remove temperatures <= current. they are pretty much useless to us.
            # we'll end up adding the current temp, so there would be no point in keeping those entries
            while stack and stack[-1][0] <= temp:
                stack.pop()

            # calculate distance to next warmer day
            if not stack: # we don't have any entries
                res.append(0)
            else:
                res.append(stack[-1][1] - i) # earliest warmer day

            # push current temperature and index
            stack.append((temp, i))

        return res[::-1]