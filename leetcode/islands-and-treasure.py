# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid or not grid[0]:
            return
            
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        
        # 2147483647 is 2^31 - 1, representing an empty room (INF)
        INF = 2147483647
        
        # 1. Initialize the queue with all gates (0)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Perform Multi-Source BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                # If neighbor is out of bounds, a wall, or ALREADY VISITED, skip it.
                # Since we only process INF cells, any cell < INF is either a wall, gate, or visited.
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == INF:
                    # Update distance and enqueue
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))

        # Complexity Analysis
        # Time Complexity O(M x N): Iterating through the entire grid once during the initialization phase to seed the queue with gates. During BFS traversal, every empty room (INF) is pushed into the queue exactly once and popped
        #                           exactly once because we instantly mutate its value away from INF. Checking the 4 directions takes O(1) time
        # Space Complexity O(M x N): Utilizing the input matrix to track our visisted state, we avoid allocating a massive O(M x N) Hash Set. However, memory footprint is still dictated by the max size of `queue`. In a worst-case
        #                            scenario in which an open grid where the BFS wave forms a massive diagonal cross-section, the queue will hold up to O(M x N) elements simultaneously