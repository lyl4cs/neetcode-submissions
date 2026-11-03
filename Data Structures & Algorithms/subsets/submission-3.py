class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Each subset is a sppecfic decision tree
        # let suse our dry run of 1 2 3 , 

        res = []
        path = []

        def backtracking(i):

            if len(nums) == i:
                res.append(path[:])
                return

            path.append(nums[i])
            backtracking(i + 1)

            path.pop()
            backtracking(i + 1)

        backtracking(0)
        return res