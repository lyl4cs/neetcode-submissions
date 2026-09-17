class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {")":"(","]":"[","}":"{"}


        for x in s:
            if x not in hm:
                stack.append(x)
            elif not stack:
                return False
            else:
                closing = stack.pop()
                if hm[x] != closing:
                    return False
        if not stack:
            return True
        else:
            return False
        