import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force would involve checking all windows and just saving the max
        
        # we can try using a heap instead (had to use hint #1)
        res = []

        for i in range(0, len(nums) - k + 1, 1):
            cur_heap = []
            for j in range(i, i + k, 1):
                heapq.heappush(cur_heap, -1 * nums[j])
            res.append(-1 * cur_heap[0])
        
        print(res)
        return 