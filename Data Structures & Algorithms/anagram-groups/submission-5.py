class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # im making the key the sorted string
        # now im adding that to the value pair each sorted string goes to corresponding key val pair
        group = defaultdict(list)

        for x in strs:
            key = "".join(sorted(x)) 
            group[key].append(x)
             
        
        return list(group.values())