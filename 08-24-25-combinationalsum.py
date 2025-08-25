class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        current = []
        res = []

        def dfs(current, current_sum, i):
            
            # match
            if current_sum == target:
                res.append(current.copy())

            # sum too high
            if current_sum > target:
                return
            
            # backtrack
            for j in range(i, len(nums)):
                current.append(nums[j])
                dfs(current, current_sum + nums[j], j)
                current.pop()
            
            return
        
        dfs(current, 0, 0)
        return res