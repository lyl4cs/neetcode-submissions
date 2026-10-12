class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need a way to input numbers besdies itself, maybe can use enumerate? 
        # need way to ignore
        # maybe can use another list to do so but this wouldnt be effiecent time
        # need a result array to try and append to.
        # ^ brute force method , implementing best solution will contnue to redo it until learned
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            # for reach indice in the result list set it to prefix
            res[i] = prefix
    # now multple for this in the nums list so the 1s are multipled
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
            