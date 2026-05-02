# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            # Take a snapshot of how many nodes are at this specific level
            level_length = len(queue)
            current_level_vals = []
            
            # Process ONLY the nodes that belong to this level
            for _ in range(level_length):
                node = queue.popleft()
                current_level_vals.append(node.val)
                
                # Add the next level's children to the back of the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # The level is finished, append it to our final result
            res.append(current_level_vals)
        
        # Complexity Analysis
        # Time Complexity O(N): Every single node in the tree is pushed into the queue exactly
        #                       once and popped exactly once. Because we are using a `deque`,
        #                       the enqueue and dequeue operations run in strict O(1) constant
        #                       time. Therefore, the overall runtime scales perfectly linearly with
        #                       the size of the tree
        # Space Complexity O(N): In a BFS, memory footprint is dictated by max width of the tree,
        #                        which is the max number of nodes sitting in the queue at any given
        #                        time. Worst-case scenario is with a perfectly balanced binary tree where
        #                        the bottom-most leaf level holds exactly N/2 nodes, which mathematically
        #                        simplifies to an O(N) memory bound
        return res