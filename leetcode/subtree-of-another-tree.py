# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Edge case: an empty subtree is technically a subtree of any tree
        if not subRoot:
            return True
        # If the main tree is empty but subRoot is not, it can't be a subtree
        if not root:
            return False
            
        # 1. If the current root matches the subRoot, trigger the deep validation
        if self.isSameTree(root, subRoot):
            return True
            
        # 2. If it wasn't a match, keep searching down the left and right branches

        # Complexity Analysis
        # Time Complexity O(R x S): In the worst-case scenario, there will be a massive main tree where
        #                           every single node has the value 1, and a subroot also filled with 1's. The outer
        #                           DFS visits R nodes, and at every single node, it triggers a full O(S) inner validation
        # Space Complexity O(H_R + H_S): Since both phases are recursive, memory footprint is dictated by the system's call
        #                                stack. The outer search goes as deep as the height of the main tree (H_R). When the
        #                                inner validation fires, it adds frames up to the height of the subtree (H_S). In
        #                                completely skewed trees, this degrades to an O(R + S) memory footprint
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Helper function to synchronously validate two trees are identical."""
        # Both reached the end simultaneously (Match)
        if not p and not q:
            return True
        
        # One reached the end before the other, or values don't match (No Match)
        if not p or not q or p.val != q.val:
            return False
            
        # Values match! Recursively check their left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)