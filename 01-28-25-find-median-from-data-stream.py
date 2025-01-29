class MedianFinder: # SOLVE AGAIN

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -1 * num)

        # print(self.max_heap)
        # print(self.min_heap)

        # If we have 2 greater than the min_heap
        # if (self.max_heap and self.min_heap and -1 * self.max_heap[0] > self.min_heap[0]):
        if (len(self.max_heap) > len(self.min_heap) + 1):
            val = heappop(self.max_heap)
            heappush(self.min_heap, -1 * val)
        
        # Right side 2 greater
        if (len(self.max_heap) + 1 < len(self.min_heap)):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -1 * val)
        
        # After balancing, ensure that the largest of max_heap is not greater than the smallest of min_heap
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val1 = heappop(self.max_heap)
            val2 = heappop(self.min_heap)
            heappush(self.max_heap, -val2)  # Move the larger value to max_heap
            heappush(self.min_heap, -val1)  # Move the smaller value to min_heap
        
            
    def findMedian(self) -> float:
        # print(self.max_heap)
        # print(self.min_heap)
        if len(self.max_heap) >len(self.min_heap):
            return -1 * self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        return (-1 * self.max_heap[0] + self.min_heap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()