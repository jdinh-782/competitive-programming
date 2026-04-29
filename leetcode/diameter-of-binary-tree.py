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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        if root.left:
            ans += 1
            stack = [root.left]

            while stack:
                node = stack.pop()

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

                if node.left or node.right:
                    ans += 1

        if root.right:
            ans += 1
            stack = [root.right]

            while stack:
                node = stack.pop()

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

                if node.left or node.right:
                    ans += 1

        # Complexity Analysis
        # Time Complexity O(N): We visit each node in the tree exactly once, where N is the number of nodes in the tree
        # Space Complexity O(H): Where H is the height of the tree. In the worst case (a completely unbalanced tree), the 
        #                        height of the tree could be N, leading to O(N) space complexity. In the best 
        #                        case (a completely balanced tree), the height would be log(N), leading to O(log N) space complexity
        return ans


    def diameterOfBinaryTreeOptimized(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def depth(node: Optional[TreeNode]) -> int:
            # Base case: an empty node has a depth of 0
            if not node:
                return 0
                
            # Recursively find the depth of the left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # The diameter passing THROUGH this current node is left + right
            # Update the global maximum diameter if this one is bigger
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return the maximum depth of THIS node to its parent
            return 1 + max(left_depth, right_depth)
            
        # Kick off the recursion
        depth(root)
        
        # Complexity Analysis
        # Time Complexity O(N): We visit each node in the tree exactly once, where N is the number of nodes in the tree
        # Space Complexity O(H): Where H is the height of the tree. In the worst case (a completely unbalanced tree), the 
        #                        height of the tree could be N, leading to O(N) space complexity. In the best 
        #                        case (a completely balanced tree), the height would be log(N), leading to O(log N) space complexity
        return self.max_diameter