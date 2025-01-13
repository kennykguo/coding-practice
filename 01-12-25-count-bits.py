class Solution:
    def countBits(self, n: int) -> List[int]:

        # n + 1 to include 0
        dp = [0] * (n + 1)

        offset = 1

        # Loops from the first index, to the last
        # eg. 0, 1, 2, 3, 4 - as indices into array, n = 4
        for i in range(1, n+1):
            # If we are currently at the offset (offset = i -> number in binary)
            # If so, then set current index to 1

            # If we have reached the next offset
            if i == 2 * offset:
                dp[i] = 1
                offset *= 2 # Multiply offset by 2
            dp[i] = 1 + dp[i - offset]
        
        print(dp)
        return dp
                

