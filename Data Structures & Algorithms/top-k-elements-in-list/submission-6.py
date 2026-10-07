class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        result = []
        for x in nums:
            hm[x] = hm.get(x, 0) + 1
        pairs = []
        for x,value in hm.items():
            pairs.append((-value, x))
        pairs.sort()
        
        for count, x in pairs[:k]:
            result.append(x)
        return result
