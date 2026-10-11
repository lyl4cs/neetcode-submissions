class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap to return count
        # can sort based on frequency of counts
        # can return sort based on K
        # i prefer to use default dictionaries because syntax is simpler to use and it will not key error u out when given empty keys
        # need result array to append k to

        from collections import defaultdict

        counts = defaultdict(int)
        result = []


        for x in nums:
            counts[x] += 1
        sorting = sorted(counts, key = counts.get, reverse = True) 
        
        # this line sorts the key in ascending order so i can then slice by k within following line

        # sorting has stored each count within my counts and has it in order now i check for the values and append

        return sorting[:k]

