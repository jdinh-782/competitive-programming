# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col_set = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        res = []
        # Initialize an empty N x N board
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r: int):
            # Base Case: We successfully placed a queen in every row
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # Try placing a queen in each column of the current row
            for c in range(n):
                # Check for conflicts in O(1) time
                if c in col_set or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                    
                # Place the queen and update our constraint sets
                board[r][c] = "Q"
                col_set.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Move to the next row
                backtrack(r + 1)
                
                # BACKTRACK: Remove the queen and clear the constraints 
                # so we can explore the next column in the current row
                col_set.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        # Start the recursive backtracking at row 0
        backtrack(0)

        # Complexity Analysis
        # Time Complexity O(N!): In the first row, we have N choices. In the second row, we have at most
        #                        N - 1 choices, then N - 2, and so on. This bounds our search space to N!. Because
        #                        our set lookups take strict O(1) time, we don't add any multiplicative overhead
        #                        to the search tree
        # Space Complexity O(N^2): Memory footprint is dictated by the N x N board matrix we use to construct the
        #                          strings, the recurisve call stack which goes exactly N layers deep, and out three
        #                          hash sets which hold up to N elements each. Thus, the auxiliary space is strictly
        #                          bounded to O(N^2)
        return res