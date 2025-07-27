import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, -1 * num)
        
    def add(self, val: int) -> int:
        # return the kth largest integer in the stream
        temp = [] # temp variable

        # push new value
        heapq.heappush(self.heap, -1 * val)

        # take out k-1 values
        for _ in range(self.k-1):
            temp.append(heapq.heappop(self.heap))
        
        # return kth value
        res = self.heap[0] * -1

        # put back k-1 values
        for i in range(len(temp)):
            heapq.heappush(self.heap, temp[i])
        return res
        

