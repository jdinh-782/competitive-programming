# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        
        # Min-heap stores tuples of: (max_elevation_on_path, row, col)
        # We start at (0, 0) with the initial water level required being grid[0][0]
        min_heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            current_time, r, c = heapq.heappop(min_heap)
            
            # If we reached the bottom-right corner, we are done!
            if r == N - 1 and c == N - 1:
                return current_time
            
            # Explore all 4 valid neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and visited state
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # The bottleneck to reach this neighbor is the MAX of the 
                    # path's current bottleneck and the neighbor's actual height.
                    max_elev = max(current_time, grid[nr][nc])
                    heapq.heappush(min_heap, (max_elev, nr, nc))
            
        # Complexity Analysis
        # Time Complexity O(N^2 log N): In the absolute worst-case scenario, we push every single cell in the grid into the Min-Heap before reaching the destination. The heap size grows up to N^2. Pushing and popping from a heap of size N^2
        #                               takes log(N^2) time, which simplifies mathematically to 2logN, or O(log N). Therefore, processing all N^2 cells scales to O(N^2 log N) time
        # Space Complexity O(N^2): The `visited` Hash Set will eventually store up to N^2 coordinate tuples to prevent infinite loops. Similarly, the `min_heap` can hold up to O(N^2) elements simultaneously in a highly balanced graph
        return -1