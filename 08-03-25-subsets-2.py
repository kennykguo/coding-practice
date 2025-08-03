class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # integers candidates
        # unique combinations that sum to target
        # each element from candidates may only be chosen once with a combination
        # no duplicate combinations



        res = []
        subset = []
        candidates.sort() # always use <variable>.sort(), if we want sorted, we need to assign it back

        def dfs(i, cur_sum):
            
            if cur_sum == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or cur_sum > target: # 0 -> len(candidates) - 1
                return
            
            subset.append(candidates[i])
            print(subset)
            dfs(i + 1, cur_sum + candidates[i])
            subset.pop()
            # remember that we can include i up to len(candidates) - 1
            # if the next element is the same as the current, then move i ahead
            # at the end, if candidates is not equal, then we still want to inc, thats why we pass in i + 1
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i + 1, cur_sum)
            return
        
        dfs(0, 0)
        print(res)
        return res

