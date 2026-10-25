# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # since im using recursion I should start with my edge cases.

        if not root:
            return 0
        
        # recrusion so calling the own function on the left and right trees

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # now time for the max depth specialty 

        return 1 + max(left,right)