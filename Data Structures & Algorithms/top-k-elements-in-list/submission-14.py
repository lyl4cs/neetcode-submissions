class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        # count into hashmap (need hm because u need number and count)
        # sort by count
        # slice by k
        dd = defaultdict(int)

        for x in nums:
            dd[x] += 1
        sorting = sorted(dd, key = dd.get, reverse = True)
        return sorting[:k]