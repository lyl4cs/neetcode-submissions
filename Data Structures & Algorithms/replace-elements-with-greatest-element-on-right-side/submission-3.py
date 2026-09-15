class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # inital max should be set to -1
        # we want to go in reverse order so we dont stack up on repeated work
        # new max = max(oldMax, arr[i])


        rightMax = -1

        for x in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[x])
            arr[x] = rightMax
            rightMax = newMax

        return arr

        
        
         
