class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)
        for x in strs:
            key = "".join(sorted(x))
            groups[key].append(x)

        return list(groups.values())