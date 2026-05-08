# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r: int, c: int, i: int) -> bool:
            # Base Case 1: We successfully matched all characters in the word!
            if i == len(word):
                return True
            
            # Base Case 2: Out of bounds, character mismatch, or already visited
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            # Mark the current cell as visited by mutating it
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            # If ANY of these paths return True, we found the word.
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # BACKTRACK: Restore the cell to its original character 
            # so other paths can potentially use it.
            board[r][c] = temp
            
            return res
        
        # Initiate DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                # Minor optimization: only trigger DFS if the first letter matches
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        # Complexity Analysis
        # Time Complexity O(N * M * 4^L): In the worst-case scenario, every single cell on the board matches the first
        #                                 letter of the word, triggering a DFS. From each cell, the DFS explores in 4
        #                                 directions, up to a maximum depth of L. While the search space theoretically
        #                                 branches out by 4^L, our eager pruning means the average runtime is drastically
        #                                 faster than this upper bound
        # Space Complexity O(L): By utilizing the in-place '#' mutation trick, we completely eliminate the need for an
        #                        O(N * M) `visited` matrix or Hash Set. Memory footprint is the maximum depth of the recurisve
        #                        call stack, which will never exceed L (length of target word)
        return False