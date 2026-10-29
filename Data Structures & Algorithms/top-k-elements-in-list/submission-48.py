class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        from collections import Counter
        count = Counter(nums)


        # go over each number, and put it's count into a bucket

        buckets = [[] for i in range(len(nums)+ 1)]

        # len(nums) + 1 since we want to include len(nums) as a bucket


        for i in range(len(nums)):
            # add to bucket the value, index by it's count

            buckets[count[nums[i]]].append(nums[i])
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            res.extend(list(set(buckets[i])))
        

        return res[:k]