class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        r = 0
        current = 0
        res = nums[0]

        if len(nums) == 1:
            return nums[0]

        # kadane's algorithm intuition:
        # once sum becomes negative, start discarding the prefix
        for i in range(len(nums)):
            current += nums[r]  # add the current number
            r += 1  # inc index
            res = max(current, res)  # check if it beats the current maximum

            # this works bcz:
            # chain of negative: will pick the closest negative to 0
            # negative sum, then positive sum -> discard negative sum, carry only the positive sum
            if current < 0:  # if negative, reset the current sum, meaning discard up to that point
                current = 0  # reset the sum

        return res
