# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # 1. Map value -> index in the inorder array for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. Global pointer to track the current root in the preorder array
        self.preorder_idx = 0
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct the subtree
            if left > right:
                return None
            
            # The current element in preorder is the root of this subtree
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            
            # Move the pointer to the next root candidate
            self.preorder_idx += 1
            
            # Find where this root splits the inorder array
            inorder_idx = inorder_map[root_val]
            
            # Recursively build the left and right subtrees.
            # CRITICAL: We must build the LEFT subtree first because the preorder 
            # traversal inherently processes left children before right children!
            root.left = array_to_tree(left, inorder_idx - 1)
            root.right = array_to_tree(inorder_idx + 1, right)
            
            return root
            
        # Kick off the recursion using the full bounds of the inorder array

        # Complexity Analysis
        # Time Complexity O(N): Creating the initial `1inorder_map` requires a single O(N) pass. During the recursion, we 
        #                       instantiate every node exactly once. Because our Hash Map provides the split index in O(1) time,
        #                       there are no nested loops or linear searches. Thus, the runtime scales strictly linearly
        # Space Complexity O(N): The `inorder_map` dictates an upfront memory footprint of O(N) to store the key-value 
        #                        pairs. Additionally, the algorithm relies on the system's Call Stack. In a perfectly 
        #                        balanced tree, the stack depth O(log N), but in the absolute worst-case 
        #                        scenario (a completely skewed tree resembling a linked list), the stack will grow 
        #                        to O(N) depth."
        return array_to_tree(0, len(inorder) - 1)