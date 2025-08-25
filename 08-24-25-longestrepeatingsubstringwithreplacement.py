class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_frequent_count = 0
        res = 0
        current_window = {}
        l = 0
        r = 0

        while r < len(s):
            
            # add char
            current_window[s[r]] = current_window.get(s[r], 0) + 1

            # most frequent count update
            most_frequent_count = max(most_frequent_count, current_window[s[r]])

            # check if we are over count
            while r - l + 1 > most_frequent_count + k:
                # pop from left until this is no longer true
                current_window[s[l]] -= 1
                l += 1

            # res saves length
            res = max(r - l + 1, res)

            r += 1
        
        return res