class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq


        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)


        while len(stones) > 1:
            # pop two largest

            stone1 = -1 * heapq.heappop(stones)
            stone2 = -1 * heapq.heappop(stones)
            if stone1 > stone2:
                heapq.heappush(stones, -1 * (stone1 - stone2))

            elif stone1 < stone2:
                heapq.heappush(stones, -1 *(stone2 - stone1))
        
        if len(stones) == 1:
            return -1 * stones[0] 
        else: return 0

        

