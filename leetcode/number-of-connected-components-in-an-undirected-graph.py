# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Initially, assume every node is its own separate component
        parent = [i for i in range(n)]
        rank = [1] * n
        
        # We start with 'n' components and decrement when we merge
        self.components = n
        
        # 1. The 'Find' function with Path Compression
        def find(node: int) -> int:
            p = parent[node]
            while p != parent[p]:
                # Path Compression: Point directly to the grandparent
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
            
        # 2. The 'Union' function with Union by Rank
        def union(n1: int, n2: int) -> None:
            p1, p2 = find(n1), find(n2)
            
            # If they already share the same root, they are already connected
            if p1 == p2:
                return
                
            # Union by Rank: Attach smaller tree under larger tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            # We successfully merged two isolated components into one
            self.components -= 1

        # 3. Process the edges
        for u, v in edges:
            union(u, v)
        
        # Complexity Analysis
        # Time Complexity O(V + E * alpha(V)): Initializing the `parent` and `rank` arrays takes O(V) time. Then, we iterate
        #                                      through the E edges. Because we paired Path Compression with Union by Rank, the
        #                                      `find` and `union` operations run in near-constant time. Theoretical bound is
        #                                      the Inverse Ackermann function alpha(V), which grows so slowly it is effectively
        #                                      <= 4 for any imaginable dataset. Thus, processing the edges takes amortized O(E) time
        # Space Complexity O(V): Adjacency list requires storing every node and every edge twice for undirected graphs, costing
        #                        O(V + E) memory. Union-Find relies exclusively on the `parent` and `rank` arrays, completely
        #                        decoupling the memory footprint from the number of edges
        return self.components