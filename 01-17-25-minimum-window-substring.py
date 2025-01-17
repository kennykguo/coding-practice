class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        cur_window_set = {} # Var #1
        window_set = {} # Var #2

        # Dictionary of reference chars
        for i in range(len(t)):
            window_set[t[i]] = window_set.get(t[i], 0) + 1

        l, r = 0, 0
        start, end = 0, 0
        res = ""
        resLen = 100000000
        window_set_count = len(window_set) # Var #5
        cur_window_count = 0 # Var #6

        # Loop until the right pointer exceeds the string length
        # Fill in with the right pointer, decrement and store max with the right pointer
        while r < len(s):
            # Fill in the cur_window dictionary
            cur_window_set[s[r]] = cur_window_set.get(s[r], 0) + 1
            # Check if the character exists in the window_set_count
            if s[r] in window_set:
                # Check if we reached the matching amount
                if window_set[s[r]] == cur_window_set[s[r]]:
                    cur_window_count += 1
            
            # Check if we match the length of the set
            if cur_window_count == window_set_count:
                while l <= r:
                    # Save the corresponding indices
                    start, end = l, r
                    if resLen > end - start + 1:
                        resLen = end - start + 1
                        res = s[start:end + 1]

                    # Start popping from the left
                    current_char = s[l]
                    cur_window_set[s[l]] = cur_window_set.get(s[l], 0) - 1
                    l += 1

                    # Check for invalid window
                    if current_char in window_set:
                        if cur_window_set[current_char] < window_set[current_char]:
                            cur_window_count-= 1
                            break
            r+= 1

        return res








