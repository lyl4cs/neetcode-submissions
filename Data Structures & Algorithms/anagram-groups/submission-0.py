class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a result hashmap
        # for each word in the str
        # I need to sort each word by their alpha. values so fit in key
        # add to hashmap
        # return the hashmap VALUES
        result = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in result:
                result[key] = [word]
            else:
                result[key].append(word)
        
        return list(result.values())
            