# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)  # N = 9
        ans = 0

        # Start from beginning of array and iterate down
        for i in range(N):            # i = 0                              i = 1
            H = height[i]             # H = height[0] = 1                  H = height[1] = 8
            left = i + 1              # left = 0 + 1 = 1                   left = 1 + 1 = 2

            limit = min(H, N-i) + 1   # limit = min(1, 9) + 1 = 2          limit = min(8, 8) = 8

            # height[i] gives us how many elements we can look up to
            while left < limit:
                R = height[left]      # R = height[1] = 8                  R = height[2] = 6
                A = min(H, R)         # A = min(H, R) = min(1, 8) = 1      A = min(8, 6) = 6
                result = A * left     # result = 1 * 1 = 1
                left += 1             # left = 1 + 1 = 2                   left = 2 + 1 = 3

            if result > ans:          # 2 > 0
                ans = result          # ans = 2
        
        # Complexity Analysis
        # Time Complexity O(N^2): Every line, we iterate through every other line to its right
        # Space Complexity O(1): Only allocating integer variables for pointers and results
        return ans


    def maxAreaOptimized(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # The width is the distance between the two pointers
            width = right - left
            # The height is bottlenecked by the shorter of the two lines
            current_height = min(height[left], height[right])
            
            # Calculate current area and update max if necessary
            current_area = width * current_height
            if current_area > max_area:
                max_area = current_area
                
            # Squeeze the pointers: ALWAYS move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # Complexity Analysis
        # Time Complexity O(N): The `left` and `right` pointers only ever move inward and never backtrack. Worst case
        #                       is when they meet in the exact middle of the array, meaning we evaluate each line
        #                       exactly one time. Execution time scales linearly
        # Space Complexity O(1): Evaluate the array entirely in place. Memory is only allocated for a few integer
        #                        variables. Memory footprint remains strictly constant, regardless of input size
        return max_area