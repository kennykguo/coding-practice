class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        print(nums)
        
        for i in range(len(nums) - 2):

            if nums[i] == nums[i-1] and i > 0: # duplicates
                continue
            print("i", i)
            l = i + 1
            r = len(nums) - 1

            while l < r:
                current_sum = nums[l] + nums[r] + nums[i]

                if current_sum == 0:
                    print(l)
                    print(r)
                    print(i)
                    res.append([nums[l], nums[r], nums[i]])
                    l+=1
                    print("l", l)
                    while nums[l] == nums[l-1] and l < len(nums) -1 :
                        l+=1

                elif current_sum > 0:
                    r -= 1
                
                else:
                    l += 1
                
        print(res)
        return res
