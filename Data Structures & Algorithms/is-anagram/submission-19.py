class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # well i can do this in two ways, I can sort them and return them compared to each other sorted but bad time complexity
        # Or I can use a hashmap and 2 for loops, Adding and subtracting each value returning boolean based on this

        from collections import defaultdict

        counts = defaultdict(int)

        for x in s:
            counts[x] +=1
    
        for x in t:
            counts[x] -=1

        for count in counts.values():
            if count != 0:
                return False
        return True