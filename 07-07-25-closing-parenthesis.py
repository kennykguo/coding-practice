class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""
        
        def dfs(cur, res, open_count, left, right):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            
            if left > 0:
                dfs(cur + "(", res, open_count + 1, left - 1, right)
            
            if right > 0 and open_count > 0:  # can only close if there are opens to match
                dfs(cur + ")", res, open_count - 1, left, right - 1)



        dfs(cur, res, 0, n, n)

        return res