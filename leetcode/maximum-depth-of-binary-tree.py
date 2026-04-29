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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Use BFS to traverse the tree level by level, counting the depth as we go
        stack = [root]
        ans = 1

        while stack:
            ans += 1
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Complexity Analysis
        # Time Complexity O(N): We visit each node in the tree exactly once, where N is the number of nodes in the tree
        # Space Complexity O(H): Where H is the height of the tree. In the worst case (a completely unbalanced tree), the 
        #                        height of the tree could be N, leading to O(N) space complexity. In the best 
        #                        case (a completely balanced tree), the height would be log(N), leading to O(log N) space complexity
        return ans


    def maxDepthOptimized(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 1

        while stack:
            node, depth = stack.pop()
            
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        # Complexity Analysis
        # Time Complexity O(N): We visit each node in the tree exactly once, where N is the number of nodes in the tree
        # Space Complexity O(H): Where H is the height of the tree. In the worst case (a completely unbalanced tree), the 
        #                        height of the tree could be N, leading to O(N) space complexity. In the best 
        #                        case (a completely balanced tree), the height would be log(N), leading to O(log N) space complexity
        return max_depth