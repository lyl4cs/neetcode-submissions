class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        bestSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num,currentSum + num)
            bestSum = max(bestSum,currentSum)

        return bestSum
