class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        cur = set()
        res = []
        n = len(nums)

        def dfs(cur_idx, numbers):

            if cur_idx >= n:
                return
            
            if sum(numbers) > target:
                return

            if sum(numbers) == target:
                res.append(numbers.copy())

            for i in range(cur_idx, len(nums)):
                numbers.append(nums[i])
                dfs(i, numbers)
                numbers.pop(-1)
        
        dfs(0, [])
        return res
            

