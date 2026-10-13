class Solution:
    def isPalindrome(self, s: str) -> bool:
        # optimal solution but mega annoying need to use 2 builtins

        l,r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum(): #if its not a alphanum skip
                l += 1
            elif not s[r].isalnum(): #if its not a alphanum skip
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
            


        