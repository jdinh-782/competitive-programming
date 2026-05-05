# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that returns the height of the tree, 
        # or -1 if an imbalance is detected anywhere below.
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            # 1. Check the left subtree
            left_height = check_height(node.left)
            # Short-circuit if the left subtree was unbalanced
            if left_height == -1:
                return -1
                
            # 2. Check the right subtree
            right_height = check_height(node.right)
            # Short-circuit if the right subtree was unbalanced
            if right_height == -1:
                return -1
                
            # 3. Evaluate current node's balance
            if abs(left_height - right_height) > 1:
                return -1
                
            # 4. If balanced, return the actual height of this node
            return max(left_height, right_height) + 1
            
        # The tree is balanced if the root doesn't return our -1 sentinel

        # Complexity Analysis
        # Time Complexity O(N): DFS guarantees that we visit every node at most once. Operations at each node take constant
        #                       O(1) time. Because of the short-circuit logic, if an imbalance is found early, the algorithm
        #                       will halt and the average-case runtime becomes significantly faster than a full O(N) sweep
        # Space Complexity O(H): Memory footprint is entirely dictated by the max depth of the recursive call stack. In a
        #                        balanced tree, the stack depth is O(log N). In the absolute worst-case scenario, there will
        #                        be a completely skewed tree resembling a linked list in which the stack size degrades to O(N) 
        return check_height(root) != -1