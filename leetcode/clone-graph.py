# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Hash map to map old nodes to their new cloned counterparts
        old_to_new = {}
        
        def dfs(curr_node):
            # Base Case / Cycle Prevention: If already cloned, return the clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]
                
            # 1. Create the clone
            copy = Node(curr_node.val)
            
            # 2. Add it to the hash map IMMEDIATELY before exploring neighbors
            # This is crucial for cycle prevention!
            old_to_new[curr_node] = copy
            
            # 3. Recursively clone and attach all neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        # Complexity Analysis
        # Time Complexity O(V + E): Because of the Hash Map, the algorithm processes each node exactly once. When visiting a node, it iterates through its adjacency list. Therefore, the time scales linearly with the total number of nodes
        #                           plus the total number of edges
        # Space Complexity O(V): Allocate auxiliary space for `old_to_new` Hash Map, which scales to exactly V entries to hold every node in the graph. Additionally, the recurisve Call Stack will go as deep as the longest path in the graph,
        #                        which in the worst case scenario is a linked-list-like straight line graph is O(V)
        return dfs(node)