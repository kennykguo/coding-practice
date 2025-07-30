class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # You should aim for a solution as good or better than O(nlogk) time and O(k) space, where n is the size of the input array, 
        # and k represents the rank of the largest number to be returned (i.e., the k-th largest element).

        # import heapq

        # for i in range(len(nums)):
        #     nums[i] *= -1

        
        # heapq.heapify(nums)


        # for i in range(k-1):
        #     val = heapq.heappop(nums)

        
        # return -1 * heapq.heappop(nums) 

        k = len(nums) - k #  target index


        def quickselect(l, r):

            # choose pivot as right always

            pivot, p = nums[r], l # pivot value is the right most value, l is the leftmost index into the array
            
            # this part of the algo only swaps if i is LESS THAN OR EQUAL TO PIVOT
            # it basically creates the right side of the partition naturally, where p ends
            # at an index where all value indices before are less than the pivot
            for i in range (l, r):
                if nums[i] < pivot: # check if we want to swap
                    nums[p], nums[i] = nums[i], nums[p] # swap pointer p with iterating pointer
                    p += 1
            
            # swap the pivot now, and check where we are in the array
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return quickselect(l, p - 1)
            
            elif p < k: return quickselect(p + 1, r)

            else: return nums[p]
        
        return quickselect(0, len(nums) - 1)


