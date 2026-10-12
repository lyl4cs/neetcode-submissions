class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        count = defaultdict(int)


        for x in s:
            count[x] += 1
        for x in t:
            count[x] -= 1

        for count in count.values():
            if count != 0:
                    return False
        return True