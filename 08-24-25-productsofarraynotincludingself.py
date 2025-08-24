class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = 1
        postfix = 1

        res = [1] * len(nums)


        for i in range(len(nums)):

            # set the prefix to the val
            res[i] *= prefix

            # multiply
            prefix *= nums[i]


        for i in range(len(nums) -1, -1, -1):

            # set the prefix to the val
            res[i] *= postfix

            # multiply
            postfix *= nums[i]
        
        return res
