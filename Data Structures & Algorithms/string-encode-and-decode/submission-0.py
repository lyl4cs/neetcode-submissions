class Solution:
    # the way this works is essntially i use # as a delimtter
    #this is used to determine when words starts / stops
    # can pull length as well and put it in front so we know how many
    # charcters to run through in it. 
    def encode(self, strs: List[str]) -> str:
        res = "" #empty result
        for x in strs: # looping for each thing in my string
            res += str(len(x)) + "#" + x # adding the string of length
        return res



    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res