class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)


        for i,x in enumerate(nums):
            secondVal = target - x
            if secondVal in count:
                return [count[secondVal],i]
            count[x] += i

