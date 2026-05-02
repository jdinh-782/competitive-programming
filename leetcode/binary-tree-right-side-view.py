# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            
            # If the current depth equals the length of our result array,
            # this is the FIRST node we are visiting at this depth.
            # Because we traverse RIGHT first, it's guaranteed to be the rightmost!
            if depth == len(res):
                res.append(node.val)
            
            # Traverse Right FIRST, then Left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        # Kick off DFS at depth 0
        dfs(root, 0)
        
        # Complexity Analysis
        # Time Complexity O(N): Recursive call will iterate through each node in the tree once. Evaluation at each node takes constant O(1) time
        # Space Complexity O(H): Memory footprint is dictated by max depth of system's recursive call stack. In a perfectly balanced tree,
        #                        max height is O(log N). Worst-case scenario will occur if a completely skewed tree resembling a linked list, then
        #                        stack size degrades to O(N)
        return res