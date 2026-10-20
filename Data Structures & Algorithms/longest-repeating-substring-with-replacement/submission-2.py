class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force solution would be checking each individual sub-string over n over again
        # im thinking to use a hashmap to find counts of something
        # whatever has the lowest count in substring, thats what we want to change
        
        seen = {}
        left = 0
        max_val = 0
        output = 0


        for right in range(len(s)):
            right_char = s[right]
            seen[right_char] = seen.get(right_char,0) + 1
            max_val = max(max_val, seen[right_char])

            while(right - left + 1) - max_val > k:
                seen[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
                
        return output