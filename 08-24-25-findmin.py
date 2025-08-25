class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0
        r = len(nums) - 1

        while l < r:
            
            mid = (l + r) // 2

            if nums[mid] > nums[r]: # pivot is on the right
                l = mid + 1
            else: # pivot is on the left
                r = mid

        return nums[l]