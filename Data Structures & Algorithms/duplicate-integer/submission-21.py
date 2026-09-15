class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        newSet = set()
        for x in nums:
            newSet.add(x)

        if len(newSet) == len(nums):
            return False
        else:
            return True

    


        

        