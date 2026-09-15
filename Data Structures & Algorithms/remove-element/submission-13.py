class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            if nums[l] != val :
                l += 1
        return l
        