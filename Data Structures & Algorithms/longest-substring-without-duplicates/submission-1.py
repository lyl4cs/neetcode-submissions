class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # no fucking clue how to do this need to come back
        seen = set()
        left = 0
        best = 0
        for right, x in enumerate(s):
            while x in seen:
                seen.remove(s[left])
                left += 1
            seen.add(x)
            best = max(best, right - left + 1)
        return best