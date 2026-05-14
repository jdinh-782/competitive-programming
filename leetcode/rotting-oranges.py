# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        fresh_oranges = 0
        
        # 1. Initialize the queue with all rotten oranges and count fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Perform Multi-Source BFS
        # Notice the 'fresh_oranges > 0' check. This acts as an early exit and
        # prevents an extra minute from being added when the final oranges are processed.
        while queue and fresh_oranges > 0:
            # Process the entire current level (representing 1 minute of time)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # If in bounds and is a fresh orange, rot it!
                    if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh_oranges -= 1
                        queue.append((row, col))
            
            # After processing all oranges for this level, increment time
            minutes += 1
            
        # Complexity Analysis
        # Time Complexity O(M x N): Iterate through the entire grid once during the initialization phase to count fresh oranges and seed the queue. During BFS traversal, every cell is pushed into the queue at most once and popped
        #                           at most once. Evaluating the 4 directions takes O(1) time per cell. Therefore, the time complexity scales strictly linearly with the number of cells
        # Space Complexity O(M x N): Memory footprint is dictated by the `queue`. Absolute worst-case scenario is where every single orange is rotten at minute 0, or the grid is structured such that almost all oranges rot
        #                            simultaneously at the very end, the queue could hold nearly M x N elements at a single time
        return minutes if fresh_oranges == 0 else -1