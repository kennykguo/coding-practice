class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # closest to the origin through euclidean distance

        # use another max heap, but we need to encode additional information in this


        import heapq
        import math
        # fact - heaps in python are sorted by the first element of a tuple


        point_tuples = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(x * x + y * y)
            point_tuples.append((distance, point))

        heapq.heapify(point_tuples)

        
        res = []
        while k > 0:
            cur = heapq.heappop(point_tuples)
            res.append(cur[1])
            k -= 1
        return res
        
        
