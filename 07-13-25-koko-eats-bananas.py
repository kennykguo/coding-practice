class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def calc_total_hours(piles, k):
            res = 0
            for val in piles:
                res += val // k
                if val % k != 0:
                    res += 1
            
            # print(k)

            return res

        
        # run a binary search on the minimum eating speed?
        piles = sorted(piles)

        mid = 0
        l = 1 # min is 1 banana/hour
        r = piles[-1] # max is # hours x max value
        
        while l < r:
            mid = (l + r) // 2 # binary search
            total_hours = calc_total_hours(piles, mid)
            print(l)
            print(r)
            
            if total_hours > h: # total hours is greater or equal to, must increase k
                l = mid + 1
            
            else:  # we have less hours, try to decrease k, but keep mid, since it could be the answer
                r = mid
            
    

        return l
            
            


