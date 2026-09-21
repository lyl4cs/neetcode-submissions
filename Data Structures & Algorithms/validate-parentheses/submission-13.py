class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"}":"{","]":"[",")":"("}

        for x in s:
            if not x in hashmap:
                stack.append(x)
            elif not stack:
                return False
            else: 
                closing = stack.pop()
                if closing != hashmap[x]:
                    return False
        return len(stack) == 0
                
      