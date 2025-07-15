class TimeMap:

    def __init__(self):
        self.name_to_val = {}
        self.name_to_time_step = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.name_to_val:
            self.name_to_val[key] = []
        self.name_to_val[key].append(value)
        if key not in self.name_to_time_step:
            self.name_to_time_step[key] = []
        self.name_to_time_step[key].append(timestamp)
        print("x", self.name_to_val)
        print("x", self.name_to_time_step)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.name_to_val:
            return ""
        else:
            # check if the time stamp can correctly be found
            if timestamp > self.name_to_time_step[key][-1]:
                return self.name_to_val[key][-1]
            elif timestamp < self.name_to_time_step[key][0]:
                return ""

            l, r = 0, len(self.name_to_time_step[key]) - 1
            
            while l < r:
                mid = (l + r + 1) // 2 
                if self.name_to_time_step[key][mid] <= timestamp: # 
                    l = mid
                else: # found value is greater, bound right side
                    r = mid - 1

            print(l) 
            if l >= 0:
                return self.name_to_val[key][l]
            else:
                return ""
            
            


# [null,null,null,null,"one","two","three"]
# ["TimeMap", "set", ["test", "one", 10], "set", ["test", "two", 20], "set", ["test", "three", 30], "get", ["test", 15], "get", ["test", 25], "get", ["test", 35]]
