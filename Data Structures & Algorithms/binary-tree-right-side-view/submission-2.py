# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            lenQ = len(q)
            levels = []
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if levels:
                res.append(levels[-1])
        return res
            
                