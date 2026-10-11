class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return a simple boolean function
        # multiple ways I can do this, I can loop through a list and add to a dict and check counts
        # I can use a set to track duplicates if order doesnt matter
        # id loop through check if it is retunr true if not return false

        seen = set()

        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
            