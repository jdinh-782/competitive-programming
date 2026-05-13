# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # 1. Mathematical Fast-Fail: A tree MUST have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        parent = [i for i in range(n)]
        rank = [1] * n
        
        # 2. 'Find' with Path Compression
        def find(node: int) -> int:
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # Compress path
                p = parent[p]
            return p
            
        # 3. 'Union' by Rank
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            
            # If they share the same parent, adding this edge creates a cycle!
            if p1 == p2:
                return False
                
            # Attach smaller tree under larger tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True
            
        # 4. Process all edges
        for u, v in edges:
            if not union(u, v):
                return False # Cycle detected
        
        # Complexity Analysis
        # Time Complexity O(N): Algorithm guarantees that it will never process more than N - 1 edges. Because the edge count is strictly bounded to N, and the `find/union` operations run in amortized O(1) time, the time complexity
        #                       shrinks to a strictly linear O(N)
        # Space Complexity O(N): Adjacency list requires O(N + E) memory to store the graph. By using Union-Find, we skip building the graph and memory footprint is perfectly flat, dictated entirely by the `parent` and `rank` arrays of size N
        return True