class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtracking(i,remain):
            if remain == 0:
                res.append(path[:])
                return
            if i == len(nums) or remain < 0:
                return

            path.append(nums[i])
            backtracking(i + 1,remain - nums[i])
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            path.pop()
            backtracking(i + 1, remain)

        backtracking(0,target)
        return res