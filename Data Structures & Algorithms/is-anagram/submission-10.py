class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        hm = defaultdict(int)

        for x in s:
            hm[x] += 1
        for x in t:
            hm[x] -= 1
        
        for count in hm.values():
            if count != 0:
                return False
        return True

        


        