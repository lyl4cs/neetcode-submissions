class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {"}":"{","]":"[",")":"("}

        for x in s:
            if x not in hm:
                stack.append(x)
            elif not stack:
                return False
            else:
                closing = stack.pop()
                if closing != hm[x]:
                    return False
        return len(stack) == 0

                    
            
            
