class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = ""
        
        for x in s:
            if x.isalnum():
                newString += x.lower()
        return newString == newString[::-1]
            
            
        