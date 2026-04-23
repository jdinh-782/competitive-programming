# Name: Johnson Dinh
# Time: 22:53
# Language: Python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0  # Row index
        left = 0
        right = len(matrix[i]) - 1  # Point to last element of first row

        while i < len(matrix):
            row = matrix[i]

            # Return early if left or right element is target
            if row[left] == target or row[right] == target:
                return True

            # Move to next row if row[right] < target
            # This will occur true at the very beginning of iteration since matrix is already sorted in ascending order
            # Note that first integer of each row is greater than last integer of previous row
            if row[right] < target:
                i += 1
                if i == len(matrix):
                    break

                left = 0
                right = len(matrix[i]) - 1
            else:
                # Retrieve midpoint element and compare to target
                mid = (left + right) // 2

                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if left > right:
                break
        
        # Complexity Analysis
        # Time Complexity O(M + log N): Where m is the number of rows and n is the number of columns in the input matrix. This is 
        #                               because we are iterating through each row and performing a binary search on each row which takes O(log n) time
        #                               Worst case is when the target is in very last row (or greater than all elements) which will make us increment i exactly M times
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return False


    def searchMatrixOptimized(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # Conceptually treat the 2D matrix as a 1D sorted array
        left = 0
        right = ROWS * COLS - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Map the 1D 'mid' index back to 2D matrix coordinates
            row = mid // COLS
            col = mid % COLS
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Complexity Analysis
        # Time Complexity O(log (M*N)): Where m is the number of rows and n is the number of columns in the input matrix
        #                               This is because we are performing a binary search on a conceptual 1D array of size M*N
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return False