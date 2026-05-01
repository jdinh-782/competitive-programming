# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, max_so_far: int) -> int:
            # Base case: if the node is empty, it contributes 0 to the count
            if not node:
                return 0
            
            # 1. Determine if the current node is "Good"
            count = 1 if node.val >= max_so_far else 0
            
            # 2. Update the maximum value seen on this path so far
            new_max = max(max_so_far, node.val)
            
            # 3. Recursively search the children, adding their "Good" counts
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count

        # The root is always compared against its own value (or -infinity)
        # We start the DFS by passing the root's value as the initial max_so_far

        # Complexity Analysis
        # Time Complexity O(N): In the worst-case scenario, we must visit every single node in the tree exactly 
        #                       once to determine if it's "Good". Each node is processed in O(1) time, leading 
        #                       to a total time complexity of O(N)
        # Space Complexity O(H): The recursive calls will dictate the maximum depth of the system's call 
        #                        stack. In a perfectly balanced tree, the height H is O(log N), but in the worst 
        #                        case (a completely skewed tree), the height can grow to O(N). Thus, the space 
        #                        complexity is O(H)
        return dfs(root, root.val)