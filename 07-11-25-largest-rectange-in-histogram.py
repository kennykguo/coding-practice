class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        res = 0

        for i in range(len(heights)):

            # stack approach
            # each new element gets its own stack
            stack = []

            # initial element
            stack.append(heights[i])
            
            # initial minimum value
            min_val = heights[i]

            # loop idx
            idx = i - 1

            # extend the rectangle only if we can find greater heights
            while idx >= 0 and heights[idx] >= min_val:
                stack.append(heights[idx])
                idx = idx - 1
                print(stack)
            
            idx = i + 1

            # extend the rectangle only if we can find greater heights
            while idx < len(heights) and heights[idx] >= min_val:
                stack.append(heights[idx])
                idx = idx + 1
                print(stack)

            res = max(res, len(stack) * min_val)
        
        return res
