class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l,r = 0,0
        # Get characters from the right, pop from the left
        # Sliding window approach
        # Store max character count at all times
        max_count = 0
        window = {}

        while r < len(s):

            # Increase the size of the current window
            window[s[r]] = window.get(s[r], 0) + 1

            # Store the max count or update it 

            max_count = max(window[s[r]], max_count)


            while (r - l + 1 - max_count > k):
                # Start popping from the left
                window[s[l]] -= 1
                l += 1
                max_count = max(window.values())
            
            res = max(r - l + 1, res)

            r+= 1
        
        return res



