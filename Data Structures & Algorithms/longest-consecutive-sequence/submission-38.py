class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set()

        for i in range(len(nums)):
            seen.add(nums[i])

        count = 0
        res = 0
        print(seen)
        for i in range(len(nums)): # loop over all numbers

            # get the value, check if it's in seen
            if nums[i] in seen:
                if nums[i] -1 not in seen:
                    count = 1
                    seen.remove(nums[i])
                    current = nums[i] + 1
                    while current in seen:
                        seen.remove(current)
                        current +=1
                        count +=1
                    res = max(res, count)
        
        return res