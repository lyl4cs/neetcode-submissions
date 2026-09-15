class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for x in s.lower():
            if x.isalnum():
                new_s += x
        
        return new_s == new_s[::-1]
                

            
            