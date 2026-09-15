class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
            

        for i, x in enumerate(nums):
            secondValue = target - x
            if secondValue in hashmap:
                return [hashmap[secondValue], i]
            hashmap[x] = i


        