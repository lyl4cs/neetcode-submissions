class Solution:
    def isValid(self, s: str) -> bool:
        match = {")":"(","}":"{","]":"["}
        stack = []

        

        for x in s:
            if x not in match:
                stack.append(x)
            else:
                if not stack:
                    return False
            if x in match:
               top = stack.pop()
               if top != match[x]:
                return False
        
        return not stack