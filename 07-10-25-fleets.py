class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range (len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key = lambda x: x[0], reverse = True)
        print(cars)
        res = len(cars)

        # process cars from front to back?
        # when car reaches end, delete it from stack
        # when car is planning to overtake other car, take it out from stack, dec res
        
        fleets = []

        while cars:
            # check if the current car can overtake the next car
            car = cars.pop(0)
            if not fleets:
                fleets.append(car)
            
            # calculate times
            ahead_car_time = (target - fleets[-1][0]) / fleets[-1][1]
            cur_car_time = (target - car[0]) / car[1]

            if cur_car_time > ahead_car_time:
                # not overtaking
                fleets.append(car)
            
        return len(fleets)
