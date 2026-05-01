# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # 1. Travel as far left as possible, pushing nodes onto the stack
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. Pop the smallest available node
            curr = stack.pop()
            k -= 1
            
            # 3. Check if it's the kth smallest
            if k == 0:
                return curr.val
                
            # 4. Move to the right child and repeat
            curr = curr.right

        # Complexity Analysis
        # Time Complexity O(H + k): In the worst case, we might have to traverse down to the leaf level of the 
        #                           tree (H) and then pop k nodes from the stack. Thus, the time complexity is O(H + k)
        # Space Complexity O(H): The stack can grow up to the height of the tree in the worst case (when the tree 
        #                        is completely skewed). In a balanced tree, the height H is O(log N), but in the worst 
        #                        case, it can be O(N). Therefore, the space complexity is O(H)