class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        bestSum = nums[0]

        for i in range(1,len(nums)):
            currentSum = max(nums[i],currentSum + nums[i])
            bestSum = max(bestSum,currentSum)

        return bestSum
