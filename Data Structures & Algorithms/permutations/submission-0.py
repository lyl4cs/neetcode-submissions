class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = [] 

        def backtracking():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtracking()
                path.pop()
        
        backtracking()
        return res
            
