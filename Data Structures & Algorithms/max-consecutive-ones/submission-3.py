class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,maxCount = 0,0
        for x in nums:
            if x == 1:
                count +=1
            else:
                count = 0
            if count > maxCount:
                maxCount = count
        return maxCount