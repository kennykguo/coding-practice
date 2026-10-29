class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        

        # prefix - left of i
        prefix = [1 for i in range(len(nums))]
        # suffix - right of i

        suffix = [1 for i in range(len(nums))]


        cur = 1
        for i in range(len(nums)):
            prefix[i] = cur
            cur *= nums[i]
        
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = cur
            cur *= nums[i]
        
        # print(prefix)
        # print(suffix)


        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums