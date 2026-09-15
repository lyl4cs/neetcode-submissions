class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newLst = []


        for numbers in nums:
            if numbers in newLst:
                return True
            newLst.append(numbers)

        return False

        