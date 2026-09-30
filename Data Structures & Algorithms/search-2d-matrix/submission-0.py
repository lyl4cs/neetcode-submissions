class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix) - 1
   
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        else:
            return False
        row = matrix[mid]    
        L,R = 0, len(row) - 1
        while L <= R:
            mid2 = (L + R) // 2
            if target == row[mid2]:
                return True
            elif target < row[mid2]:
                R = mid2 - 1
            else:
                L = mid2 + 1
        return False



        