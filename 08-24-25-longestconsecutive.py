class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for num in numset:

            if num - 1 not in numset:
                # start of seq
                current_count = 0 # init 0
                current_val = num # current num is a start

                # loop to find how many there are
                while current_val in numset:
                    current_count += 1
                    current_val += 1
                    res = max(res, current_count)

        
        return res
