# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(n: int) -> int:
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
                
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True
            
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        # Complexity Analysis
        # Time Complexity (O(N * alpha(N))): The `find` and `union` operations run in near-constant time. The theoretical bound is the
        #                                    inverse Ackermann function alpha(N). Because alpha(N) grows so slowly that it is <= 4 for
        #                                    any realistically imaginable dataset in the universe, the operations are amortized O(1)
        # Space Complexity O(N): Memory footprint is dictated entirely by the `parent` and `rank` arrays, both of which scale linearly
        #                        to the number of nodes
        return []