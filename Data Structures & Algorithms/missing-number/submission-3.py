class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for numbers in range(0 , len(nums) + 1):
            if numbers not in nums:
                return numbers
