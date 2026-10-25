class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort attempt 1
        from collections import defaultdict
        
        count = defaultdict(int)
        for x in nums:
            count[x] += 1 

        buckets = [[] for x in range(len(nums) + 1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        
        res = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
