class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def dfs(l, r):
            if l == r:
                return nums[l]

            left = nums[l] - dfs(l + 1, r)
            right = nums[r] - dfs(l, r - 1)

            res = max(left, right)
            return res

        return True if dfs(0, len(nums) - 1) >= 0 else False
