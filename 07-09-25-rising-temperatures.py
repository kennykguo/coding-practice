class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # needs to be the closest future day
        # brute force is obviously n^2
        # reverse approach from hint #2
        stack = []
        indices = []

        cur_min = temperatures[0]

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # add to stack if the current element is greater than the cur_min of the element seen
            if temperatures[i] <= cur_min: 
                # if the value is less than or equal to the cur_min, 
                # not what we are looking for, we should add to the stack
                cur_min = temperatures[i]
                stack.append(temperatures[i])
                indices.append(i)

                # this means that the stack is in descending order
            else: # we found a value greater than the cur_min of the stack
                # we should start popping until we find a value greater than our current temperature
                # or stack is empty
                while stack and stack[-1] < temperatures[i]:
                    print(stack)
                    print(indices)
                    
                    # pop a value from the stack
                    val = stack.pop()

                    # pop the corresponding index
                    idx = indices.pop()

                    res[idx] = i - idx
                
                stack.append(temperatures[i])
                indices.append(i)
                cur_min = temperatures[i]
        
        return res
                    

                    