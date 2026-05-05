# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are None. They match structurally and hold no value.
        if not p and not q:
            return True
            
        # Base Case 2: One node is None but the other isn't (Structure mismatch), 
        # OR both exist but their values are different (Value mismatch).
        if not p or not q or p.val != q.val:
            return False
            
        # If we made it here, the current nodes match perfectly.
        # Now, recursively verify that BOTH the left branches AND right branches match.

        # Complexity Analysis
        # Time Complexity O(N): Absolute worst-case scenario is when both trees are perfectly identical, the algorithm
        #                       must visit each single node to confirm the match. The structural and value comparisons
        #                       at each node execute in strict O(1) constant time. However, due to short-circuiting logic, the
        #                       average-case runtime is often much faster if a mismatch is found near the top of the three
        # Space Complexity O(H): In perfectly balanced trees, the stack height is O(log N). In the absolute worst-case scenario,
        #                        there are completely skewed trees resembling linked lists, the stack size degrades to O(N)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)