# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        
        # Helper function to compute area and sink the island
        def dfs(r: int, c: int) -> int:
            # Base Case: out of bounds OR water (0)
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 0
            
            # Mark the current cell as visited by "sinking" it (mutating to 0)
            grid[r][c] = 0
            
            # The area is 1 (current cell) + the area of all 4 connected neighbors
            return (1 + 
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))

        # Scan every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # Only trigger DFS if we find land
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)
        
        # Complexity Analysis
        # Time Complexity O(M x N): Iterate through every cell in the grid via the nested loops. When a 1 is found, the DFS explores it and immediately mutates it to 0. Because a cell is only over processed as a 1 exactly once,
        #                           no cell is evaluated by the DFS more than a constant number of times (checked once by the main loop and up to 4 times by adjacent neighbors). Therefore, the time complexity scales strictly 
        #                           linearly with the size of the grid
        # Space Complexity O(M x N): By utilizing in-place mutation (`grid[r][c] = 0`), we achieve O(1) external memory for tracking visited states. the absolute worst-case scenario, where the entire grid is a single contiguous 
        #                            island forming a winding, snake-like path—the recursion will sink M x N levels deep before unwinding
        return max_area