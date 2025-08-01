class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0

        import heapq

        # of total unique tasks is FIXED - A - Z
        # hint # 1 - how do we determine which task should be processed first?
        # process one with largest freq to get it out of the way

        frequency = {}
        for task in tasks:
            frequency[task] = frequency.get(task, 0) + 1
        print(frequency)

        most_frequent = []
        for task in frequency:
            heapq.heappush(most_frequent, (-frequency[task], task))
        print(most_frequent)

        q = []
        # (freq, key)
        # simulation
        # heaps are immutable!
        while most_frequent or q:

            res += 1
            if most_frequent: # if we have elements
                val = heapq.heappop(most_frequent) # pop from top -> (freq, key)
                new_val = (val[0]*-1 - 1, val[1])

                # add it to the q
                if new_val[0] > 0:
                    q.append((new_val, res + n)) # -> [(entry, time),,,]

            
            # check for moving back to the task scheduler
            while q and q[0][1] <= res:
                val = q.pop(0)
                val = val[0]
                new_val = (val[0] * -1, val[1])
                heapq.heappush(most_frequent, new_val)
        
        return res

            
