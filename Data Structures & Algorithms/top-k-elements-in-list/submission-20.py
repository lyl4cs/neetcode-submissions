class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)

        for x in nums:
            count[x] += 1
        sort = sorted(count, key = count.get , reverse = True)

        return sort[:k]