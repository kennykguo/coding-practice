from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        total = total // 2
        dp = [True] + [False] * total

        for num in nums:
            for i in range(total, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[total]
