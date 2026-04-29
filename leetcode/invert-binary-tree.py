# Name: Johnson Dinh
# Time: 4:04
# Language: Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        temp = root
        
        # Store current left and right nodes
        l = root.left
        r = root.right

        # Swap left and right nodes
        root.left = r
        root.right = l

        self.invertTree(root.left)
        self.invertTree(root.right)

        # Complexity Analysis
        # Time Complexity O(N): Method visits every node in the tree exactly once, where N is the number of nodes in the tree
        # Space Complexity O(H): Where H is the height of the tree. In the worst case (a completely unbalanced tree), the 
        #                        height of the tree could be N, leading to O(N) space complexity. In the best 
        #                        case (a completely balanced tree), the height would be log(N), leading to O(log N) space complexity
        return temp


    def invertTreeOptimized(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case
        if not root:
            return None
            
        # Swap the left and right children using tuple unpacking
        root.left, root.right = root.right, root.left
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Complexity Analysis
        # Time Complexity O(N): Method visits every node in the tree exactly once, where N is the number of nodes in the tree
        # Space Complexity O(H): Where H is the height of the tree. In the worst case (a completely unbalanced tree), the 
        #                        height of the tree could be N, leading to O(N) space complexity. In the best 
        #                        case (a completely balanced tree), the height would be log(N), leading to O(log N) space complexity
        return root