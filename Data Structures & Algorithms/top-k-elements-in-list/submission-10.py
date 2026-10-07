class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #attemting the use of DEFAULT DICT
        from collections import defaultdict

        hm = defaultdict(int)

        for x in nums:
            hm[x] += 1
        
        return sorted(hm, key= hm.get , reverse = True)[:k]
            
