# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        total_cost = 0
        visited = set()
        
        # Min-heap stores tuples of: (cost_to_reach, point_index)
        min_heap = [(0, 0)]
        
        # We stop the exact moment all N points are connected
        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            
            # Cycle prevention: If we already connected this point, discard the edge
            if i in visited:
                continue
                
            # 1. Connect the point and add to total cost
            visited.add(i)
            total_cost += cost
            
            # 2. Calculate distances to all UNVISITED points and add to the heap
            for j in range(N):
                if j not in visited:
                    # Manhattan Distance formula: |x1 - x2| + |y1 - y2|
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (dist, j))
        
        # Complexity Analysis
        # Time Complexity O(N^2 log N): In the worst case, very time we process a node, we calculate the distances to all other unvisited nodes and push them into the heap. The heap can grow to hold
        #                               up to O(N^2) edges. Popping from a heap of size N^2 takes log(N^2) time, which simplifies mathematically to 2 log N. Therfore, the total time complexity scales
        #                               to O(N^2 log N)
        # Space Complexity O(N^2): The `visited` set takes O(N) space, but the `min_heap` acts as our memory bottleneck, potentially holding up to O(N^2) redundant edges simultaneously before they
        #                          are popped and discarded
        return total_cost