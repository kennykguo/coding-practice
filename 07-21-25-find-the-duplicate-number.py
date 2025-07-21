class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        # solve the problem without modifying the array and using O(1) space

        # key is that the elements in the given array are within the range 1 to len(nums)

        # approach - take a sum? 

        # use given array as a hash set without creating a new one?

        # marking positions corresponding to elements that have already been countered

        # nums.sort()

        # for i in range(n):
        #     if nums[abs(nums[i]) - 1] < 0:
        #         return abs(nums[i])
        #     else:
        #         nums[abs(nums[i]) - 1] *= -1
        #         print("here")
        
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow

