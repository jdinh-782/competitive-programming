# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        return dfs()
    

    # Complexity Analysis
    # Time Complexity O(V): For serialization, we visit every node (and every empty child pointer) exactly 
    #                       once. For deserialization, we process every token in the split string exactly 
    #                       once. The string `join`` and split operations also run in O(V) time
    # Space Complexity O(V): During serialization, we allocate an array of size 2V + 1 (nodes + null markers)
    #                        to hold the string tokens.During deserialization, the .split(",") operation creates 
    #                        an array of that same size. Additionally, the auxiliary space used by the recursive 
    #                        call stack scales with the height of the tree, O(H), which in the worst 
    #                        case (a completely skewed tree) degrades to O(V)