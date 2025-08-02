class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        # nums = [1,2,3]
        # dfs(nums, [], 0)
        # what is a subset? 

        def dfs(nums, cur, cur_idx):
            
            if cur_idx == len(nums) + 1:
                return

            # backtrack + recursion
            for i in range(cur_idx, len(nums)):
                cur.append(nums[i])
                dfs(nums, cur, i+1)
                cur.pop()
                
            nonlocal res
            res.append(cur.copy())
            return
        
        dfs(nums, [], 0)
        return res
