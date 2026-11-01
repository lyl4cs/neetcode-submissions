"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if node is None:
            return None

        # Map each original node to its new copy.
        copies = {node: Node(node.val)}
        q = deque([node])

        while q:
            original = q.popleft()

            for neighbor in original.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # Connect the current copy to the neighbor's copy.
                copies[original].neighbors.append(copies[neighbor])

        return copies[node]