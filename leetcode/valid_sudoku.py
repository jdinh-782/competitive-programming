# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each sublist in `board` is already a row
        for row in board:
            # Compare length of original row with length of set(row)
            parsed_row = [r for r in row if r != "."]

            if len(parsed_row) != len(set(parsed_row)):
                return False

        # Transpose matrix to analyze columns
        board_T = [list(row) for row in zip(*board)]
        for col in board_T:
            # Compare length of original col with length of set(col)
            parsed_col = [c for c in col if c != "."]

            if len(parsed_col) != len(set(parsed_col)):
                return False

        # Analyze 3x3 sub-boxes
        i = 0
        j = 0
        while True:
            box = board[i][j:(j+3)]
            box.extend(board[i+1][j:(j+3)])
            box.extend(board[i+2][j:(j+3)])
            
            # Compare length of box values with length of set(box)
            parsed_box = [b for b in box if b != "."]

            if len(parsed_box) != len(set(parsed_box)):
                return False

            if i == 6:
                break

            if j == 6:
                i += 3
                j = 0
            else:
                j += 3
        
        # Complexity Analysis
        # Time Complexity O(N^2): Solution iterates through the 81 cells, 3 separate times. Analyses for row takes O(N^2), transpose takes O(N^2), and box takes O(N^2)
        #                         which results in O(3N^2) -> O(N^2), performing 3 distinct passes
        # Space Complexity O(N^2): Bottleneck occures when trying to transpose the original `board` array to analyze columns. This completely copies the entire 2D array
        #                          into a new block of memory just to read the columns
        return True

    
    def isValidSudokuOptimized(self, board: List[List[str]]) -> bool:
        # Initialize an array of 9 empty sets for rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Calculate which of the 9 boxes we are currently in
                # r // 3 -> Identifies which "row of boxes" we are in (top, middle, bottom)
                # (r // 3) * 3 -> Provides us with the starting index of the row
                # c // 3 -> Identifies the horizontal offset within that row
                box_idx = (r // 3) * 3 + (c // 3)
                
                # If we've seen this value in the current row, col, or box, it's invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Otherwise, register the value into our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        
        # Complexity Analysis
        # Time Complexity O(N^2): Solution iterates through the 9x9 grid exactly one time, resulting in O(N^2) runtime. Checking a Python set for a value and adding a
        #                         value to a set both execute in O(1) time on average. Execution speed scales linearly with total number of cells on the board
        # Space Complexity O(N^2): Maintaining three arrays of sets, at the worst case, will be a completely full board with each of the N rows, N columns, and N boxes
        #                          will store N elements. Therefore, memory scales directly with the size of the board    
        return True