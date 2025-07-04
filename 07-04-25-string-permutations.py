class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        set1 = {}
        set2 = {}

        for i in range(len(s1)):
            set1[s1[i]] = set1.get(s1[i], 0) + 1

        for i in range(len(s2)):
            set2[s2[i]] = set2.get(s2[i], 0) + 1
        
        # check permutations now
        for i in range(len(s2)):
            # check at each index
            cur_char = s2[i]

            # check for current char in set1's keys
            if cur_char in set1.keys():
                
                # logic for determining permutation
                set1_copy = set1.copy() # deep copy
                num_elements = len(set1) # number of total unique characters
                cur = i # current index for looping

                # go through next few elements, until num_elements is zero
                while (num_elements!=0):
                    
                    # if out of bounds, break out of while loop
                    if cur >= len(s2) or s2[cur] not in set1_copy.keys():
                        break
                    
                    # current element is valid + decrement in the list
                    set1_copy[s2[cur]] = set1_copy[s2[cur]] - 1

                    # decrement count if cur char's count is 0
                    if set1_copy[s2[cur]] == 0:
                        num_elements = num_elements - 1
                        set1_copy.pop(s2[cur])
                    
                    cur += 1
                
                if len(set1_copy) == 0:
                    return True                          
        
        return False
