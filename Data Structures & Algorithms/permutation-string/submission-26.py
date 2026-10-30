class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dict1 = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
        dict2 = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
        for i in range(len(s1)):
            dict1[s1[i]] = dict1.get(s1[i], 0) + 1
        for i in range(len(s2)):
            dict2[s2[i]] = dict2.get(s2[i], 0) + 1
        print(dict1)
        print(dict2)

        # sliding window check
        running = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
        if len(s1) > len(s2):
            return False
        
        # initial window
        for i in range(len(s1)):
            running[s2[i]] = running.get(s2[i], 0) + 1
        l = 0
        r = len(s1) - 1
        print(running)

        #abc
        # each window, count the # of matches
        while r < len(s2):
            print(r)
            if running == dict1:
                return True
            
            r+=1
            if r == len(s2):
                break
            running[s2[r]] += 1
            running[s2[l]] -= 1
            l+=1
        
        print(running)
        return False