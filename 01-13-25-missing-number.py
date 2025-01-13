class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums)) * (len(nums)+ 1) / 2
        print(total)
        for i in range(len(nums)):
            total -= nums[i]
        return int(total)
