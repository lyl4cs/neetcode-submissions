class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = []
       
        for x in nums:
            if x in nums1:
                return True
            else:
                nums1.append(x)

        return False

            
