class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        # Counter(nums) maps numbers to their frequencies

        count = Counter(nums)
        # print(count)
        buckets = [[] for i in range(len(nums)+1)] # each index stores the count, each list stores the number

        # print(len(count))
        for idx in range(len(nums)):
            # print(count[nums[idx]])
            buckets[count[nums[idx]]].append(nums[idx])
        
        res = []
        # print(buckets)
        for i in range(len(nums), -1, -1):
            # print(list(set(buckets[i])))
            res.extend(list(set(buckets[i])))
        
        
        return res[:k]