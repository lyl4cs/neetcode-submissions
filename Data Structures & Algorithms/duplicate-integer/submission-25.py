class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pen = set()
        
        
        for x in nums:
            if x in pen:
                return True
            pen.add(x)
        return False



        