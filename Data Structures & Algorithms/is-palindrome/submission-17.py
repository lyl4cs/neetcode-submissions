class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleanedS = ""
         
        for x in s:
            if x.isalnum():
                cleanedS += x

        return cleanedS.lower() == cleanedS.lower()[::-1]

            
