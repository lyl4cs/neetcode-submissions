class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)

        for x in nums:
            count[x] += 1
        
        assorted = sorted(count , key = count.get , reverse = True)

        return assorted[:k]
        