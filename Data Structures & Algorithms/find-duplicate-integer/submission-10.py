class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while True:
            
            slow = nums[slow]
            fast = nums[nums[fast]]

            # check after moving
            if slow == fast:
                break

            # the first meeting point may be anywhere inside the cycle. after ptrs meet
        
        second = 0
        
        while slow != second:
        
            slow = nums[slow]
            second = nums[second]


        return slow

