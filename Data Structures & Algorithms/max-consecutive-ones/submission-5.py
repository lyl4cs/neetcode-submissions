class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # im going to need a max count value basically
        # read through the nums array with a loop adding a count for every 1 and resetting the count at 0.
        count = 0
        maxCount = 0
        for x in nums:
            if x == 1:
                count +=1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0
        return maxCount
