class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(i,remain):
            if remain == 0:
                res.append(path[:])
                return
            if i == len(nums) or remain < 0:
                return

            path.append(nums[i])
            backtracking(i,remain - nums[i])

            path.pop()
            backtracking(i + 1, remain)

        backtracking(0,target)
        return res