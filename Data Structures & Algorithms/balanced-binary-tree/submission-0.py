# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # my thought is to try and get the height and then do a comparsion opperator like >= by 1 or smth
        balanced = True
        
        def dfs(node):
            # need to get height
            # need to call on each node nost just root
            nonlocal balanced

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            height = 1 + max(left,right)

            if abs(left - right) > 1:
            
                balanced = False
            return height
        dfs(root)
        return balanced
                        
