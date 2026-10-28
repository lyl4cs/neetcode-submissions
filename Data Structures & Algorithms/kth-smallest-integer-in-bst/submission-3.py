# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None
        def dfs(node):
            if not node:
                return 0

            nonlocal count,answer
            dfs(node.left)
            count += 1

            if count == k:
                answer = node.val
            dfs(node.right)



        dfs(root)    
        return answer