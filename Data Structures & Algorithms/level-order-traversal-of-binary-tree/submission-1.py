# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque #import deque / need for BFS

        res = [] # final answer is a result based on a list of levels so need

        q = deque() #make the queue
        q.append(root) # append the root to it to get started

        while q: #obvious, keep going while theres nodes to be visited
            qLen = len(q) #locking the size of this level only processing cur
            level = [] 
            for i in range(qLen):
                node = q.popleft() #pop exactly qlen nodes out,curr lev,front
                if node: # if the node isnt null
                    level.append(node.val) # Root note 1 in this case
                    q.append(node.left) 
                    q.append(node.right)
            if level:
                res.append(level) # save the level
        return res