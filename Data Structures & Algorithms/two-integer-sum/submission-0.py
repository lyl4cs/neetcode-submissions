class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # so i need to scan through this list, probably storing
        # - both the actual input number snd the input its self
        # i can prob do that wiht a set and using get keys n value
        # so we can probably take the given target subtract it 
        # by the first value and look for the other value that makes the equation equal to

        dictionary = {}

        for i, x in enumerate(nums):
            secondVal = target - x
            if secondVal in dictionary:
                return [dictionary[secondVal], i]
            dictionary[x] = i

