# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        # Helper function to run DFS and mark safe connected regions
        def capture_safe_regions(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
                return
            
            # Mark the current 'O' as 'T' (Safe/Temporary)
            board[r][c] = 'T'
            
            # Explore all 4 adjacent directions
            capture_safe_regions(r + 1, c)
            capture_safe_regions(r - 1, c)
            capture_safe_regions(r, c + 1)
            capture_safe_regions(r, c - 1)
            
        # 1. Capture unsurrounded regions (Start from borders)
        for r in range(ROWS):
            for c in range(COLS):
                # Only trigger DFS if we are on the boundary and find an 'O'
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    capture_safe_regions(r, c)
                    
        # 2. Iterate over the entire board to finalize the state
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    # It was never reached by the boundary DFS, so it's surrounded
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    # It was a safe region, revert it back to 'O'
                    board[r][c] = 'O'

        # Complexity Analysis
        # Time Complexity O(M x N): In the absolute worst-case scenario, where the entire board is filled with '0', the boundary loop triggers a DFS that visits every single cell on the board exactly once. The
        #                           final cleanup loop also visits every cell once. Because we immediately change visited cells to 'T', we never process the same cell twice. Therefore, time scales strictly linearly
        #                           with the number of cells
        # Space Complexity O(M x N): Because this algorithm alters the matrix in-place, we don't need to allocate an external `visited` Hash set or a duplicate matrix, keeping external memory at O(1). However, the
        #                            recursive DFS utilizes the system's call stack. In the worst case, a massive, winding snake-like path of '0' covering the whole board, the recursion depth could reach O(M x N)