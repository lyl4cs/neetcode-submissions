class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        hm = defaultdict(int)

        for i,x in enumerate(nums):
            secondVal = target - x
            if secondVal in hm:
                return [hm[secondVal],i]
            hm[x] = i
                