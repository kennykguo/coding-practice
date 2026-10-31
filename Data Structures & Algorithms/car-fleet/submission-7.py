class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # dst at target
        # a car cannot pass another car ahead of it
        # catch up and drive at the same speed
        # [4,1,0,7]
        # [3,5,10,3]
        res = 0
        sorted_positions = sorted(position)
        sorted_speeds = [v for k,v in sorted(zip(position, speed))]
        # time = (target - position) / speed



        # print("pos", sorted_positions)
        # print("speed", sorted_speeds)
        times = []
        for i in range(len(position)):
            times.append((target - sorted_positions[i]) / sorted_speeds[i])
        # print(times)



        stack = []

        for i in range(len(times)-1, -1, -1):
            cur = times[i] # current time
            # stack stores the longest time. compare entry, and then check if cur entry has
            # shorter time than the current max that means it'll join a fleet
            # if the time is longer, then append it, also means another fleet
            if not stack:
                res+=1
                stack.append(cur)
            elif stack and stack[-1] < cur:
                res+=1
                stack.append(cur)
            # eg. 4, 3, 5
            # from r to l
            # for 5, stack is empty, so add a fleet, and append current value
            # for 3, current value is less, so don't do anything
            # for 4, current value is less, don't do anything


        return res


