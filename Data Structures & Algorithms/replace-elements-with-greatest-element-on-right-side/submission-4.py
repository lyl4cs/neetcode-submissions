class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for x in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[x])
            arr[x] = rightMax
            rightMax = newMax

        return arr
