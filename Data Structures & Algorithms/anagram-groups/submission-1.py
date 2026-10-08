class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # use default dict as list format because i need to send as lst
        # try and sort the inputs from the list and use that as key
        # append the values to the new list
        dd = defaultdict(list)

        for x in strs:
            key = "".join(sorted(x))
            if key not in dd:
                dd[key] = [x]
            else:
                dd[key].append(x)
        return list(dd.values())
        