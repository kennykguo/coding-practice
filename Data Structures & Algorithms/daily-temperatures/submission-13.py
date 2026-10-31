class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        stack = []
        length = len(temperatures) - 1

        for i in range(length, -1, -1):
            # print(temperatures[i])
            # print(stack)

            while stack and temperatures[stack[-1]] <= temperatures[i]: # stack exists, and current temp is greater
                stack.pop()


            if stack: # no elements in stack
                res.append(stack[-1]-i)
            else:
                res.append(0)

            stack.append(i)
        
        # print(res)
        # print(stack)
        return res[::-1]