class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three pointer method

        nums.sort()
        print(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            print(i)

            # skip i entries that are repeats
            l = i + 1
            r = len(nums) - 1 # indices

            
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0: # add to result variable
                    res.append([nums[i], nums[l], nums[r]])
                    # avoid duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                
                if nums[i] + nums[l] + nums[r] > 0: # too high
                    r -= 1
                
                else: # too low
                    l += 1
            
        return res

