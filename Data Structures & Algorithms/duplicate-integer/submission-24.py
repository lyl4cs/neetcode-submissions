class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        memory = set()

        for x in nums:
            if x in memory:
                return True
            memory.add(x)
        
        return False

      
            

    

            
        