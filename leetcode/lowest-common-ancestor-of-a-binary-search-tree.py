# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both p and q are greater than parent, go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            # If both p and q are less than parent, go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            # We have found the split point (or one of the nodes is the parent)
            else:
                return curr

        # Complexity Analysis
        # Time Complexity O(H): Executing a simple linear search down a single path from the root
        #                       to the LCA. Completely ignore the other halves of the tree at every
        #                       step. In a perfectly balanced BST, the height is O(log N). In the
        #                       absolute worst-case scenario is with a completely skewed tree
        #                       resembling a linked list in which the traversal could take O(N) time
        # Space Complexity O(1): Explicitly choosing an iterative `while` loop, we completely avoid
        #                        allocating any memory on the system's call stack