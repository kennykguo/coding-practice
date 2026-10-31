class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        waiting, out = [], [0] * len(temperatures) # default is 0
        for i, value in enumerate(temperatures): # idx, and val in temperatures
            # waiting stores indices of the temperatures that do not have a warmer day yet set
            # if the current temperature is warmer,
            while waiting and temperatures[waiting[-1]] < value: # current temperature is greater:
                j = waiting.pop() # index of that current val
                out[j] = (i-j)
            waiting.append(i)
        
        # print(out)
        return out