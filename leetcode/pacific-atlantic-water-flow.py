# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # Helper function to run Reverse DFS
        def dfs(r, c, reachable_set, prev_height):
            # Base cases: out of bounds, already visited, or going strictly downhill (invalid for reverse flow)
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                (r, c) in reachable_set or 
                heights[r][c] < prev_height):
                return
            
            # Mark as reachable
            reachable_set.add((r, c))
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        # 1. Trigger DFS from the Pacific and Atlantic coastlines
        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])               # Pacific Top Row
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c]) # Atlantic Bottom Row
            
        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])               # Pacific Left Column
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1]) # Atlantic Right Column
            
        # 2. Find the intersection of both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r, c])
        
        # Complexity Analysis
        # Time Complexity O(M x N): Absolute worst-case scenario, a completely flat grid, the Pacific DFS visits every cell exactly once, and the Atlantic DFS visits every cell exactly once. Same cell does not get processed twice
        #                           for the same ocean, the time complexity remains strictly linear with respect to the total number of cells in the grid
        # Space Complexity O(M x N): Maintaining two Hash Sets which, in the worst case, will both store every cell coordinate in the grid, taking O(M x  N) space. Additionally, the recursive Call Stack for the DFS could reach
        #                            a max depth of M x N if the heights form a single, winding uphill snake-path
        return res