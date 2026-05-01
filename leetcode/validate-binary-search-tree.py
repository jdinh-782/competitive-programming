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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to pass down our dynamic boundaries
        def validate(node: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
            # Base case: an empty node is technically a valid BST
            if not node:
                return True
            
            # The current node's value must fall strictly inside the bounds
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively validate both subtrees:
            # - Left child inherits the current node's value as its new MAXIMUM
            # - Right child inherits the current node's value as its new MINIMUM
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        # Complexity Analysis
        # Time Complexity O(N): In the worst-case scenario, the tree is a perfectly valid BST, our algorithm must visit every
        #                       single node exactly once to verify it. Mathematical evaluation at each node takes strict O(1) time
        # Space Complexity O(H): Recursive calls will dictate the max depth of the system's call stack where in a perfectly
        #                        balanced tree, the height H is O(log N), but in the worst case (a completely skewed tree),
        #                        the height can grow to O(N). Thus, the space complexity is O(H)
        return validate(root)