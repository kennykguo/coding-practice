class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) -1

        while l<=r:
            

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # are we in the left side or the right side of the array
            if nums[mid] >= nums[l]: # mid is on the left side
                if target > nums[mid] or target < nums[l]: # greater
                    l = mid + 1
                else:
                    r = mid - 1

            else: # mid is on the right side
                if target < nums[mid] or target > nums[r]: # greater
                    r = mid - 1
                else:
                    l = mid + 1



        return -1