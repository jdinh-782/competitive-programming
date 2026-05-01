# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize our global max tracker to negative infinity
        self.global_max = float('-inf')
        
        def get_max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            # 1. Traverse down to the leaves. 
            # If a path is negative, we prune it by returning 0 (ignoring it).
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))
            
            # 2. Calculate the max path sum if this node is the highest point of the path
            current_local_path_sum = node.val + left_gain + right_gain
            
            # 3. Update the global max if our local path is better
            self.global_max = max(self.global_max, current_local_path_sum)
            
            # 4. Return the max gain this node can provide to its parent.
            # It can only offer itself + its best single branch.
            return node.val + max(left_gain, right_gain)
            
        # Kick off the DFS
        get_max_gain(root)
        
        # Complexity Analysis
        # Time Complexity O(N): The recursive call visits every single node in the tree exactly once. Operations performed
        #                       at each node execute in constant O(1) time, yielding a strictly linear runtime
        # Space Complexity O(H): Memory footprint is entirely dictated by maximum depth of the recurisve call stack. In a perfectly
        #                        balanced tree, height is log_2(N), resulting in O(log N) space complexity
        #                        In the worst case, a completely unbalanced tree (like a linked list), height is N, resulting in O(N) space complexity
        return self.global_max