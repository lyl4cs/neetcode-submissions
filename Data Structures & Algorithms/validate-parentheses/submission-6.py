class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(","}":"{","]":"["}
        stack = []


        for x in s:
            if x in "({[":
                stack.append(x)
            elif not stack:
                    return False
            else:
                closing = stack.pop()
                if dictionary[x] != closing:
                    return False
        if not stack:
            return True
        else:
            return False