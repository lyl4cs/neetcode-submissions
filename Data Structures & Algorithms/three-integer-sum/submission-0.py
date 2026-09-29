class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i,x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue

            L,R = i + 1,len(nums) - 1
        
            while L < R:
                total = x + nums[L] + nums[R]
                if total == 0: 
                    result.append([x, nums[L],nums[R]])
                    L += 1 
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                if total < 0:
                    L += 1 
                if total > 0:
                    R -= 1
        return result