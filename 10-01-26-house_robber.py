class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = 0
        res = 0

        for i in range(0, len(nums)):  # iterate over houses
            tmp = res
            res = max(prev + nums[i], res)
            prev = tmp

        return res
