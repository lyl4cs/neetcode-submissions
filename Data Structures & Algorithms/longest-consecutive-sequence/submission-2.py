class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # im thinking wed want to sort this because its prob be easier?
        # what does this mean for time complexity though?
        # check values for every thing if its +1 then add 1 to a count
        # return count?
        # need to track longest
        # need to start count at 1 
        # when comparing to prev variables u cant start at zero
        # u can also look forward though so itd be nums i+1
        # O(n log n) solution because im sorting 
        # (Brute Force sol.)
        
        nums.sort() 
        if not nums:
            return 0
        curr = 1
        longest = 1
        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                    curr = 1
            if curr > longest:
                longest = curr
        return longest

