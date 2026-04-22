# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        ans = 0
        s = []

        for i in range(len(heights)):
            length = heights[i]
            width = 1
            area = length * width

            # Early check if bar itself is largest rectangle
            if area > ans:
                ans = area

            s.append(heights[i])
            # s = [2]

        # Complexity Analysis
        # Time Complexity O(N): We have an outer loop that iterates through each bar exactly once
        # Space Complexity O(N): In the worst case, if the heights are in increasing order, we will push all of them onto the stack `s`
        return ans


    def largestRectangleAreaOptimized(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Will store tuples of: (start_index, height)
        
        for i, h in enumerate(heights):
            start = i
            
            # If the current height is shorter than the top of our stack, the taller rectangles are "cut off" and must be resolved
            while stack and stack[-1][1] > h:
                pop_index, pop_height = stack.pop()
                
                # Calculate the area of the rectangle we just cut off
                max_area = max(max_area, pop_height * (i - pop_index))
                
                # The current shorter bar can extend backwards into the space 
                # of the taller bar we just popped
                start = pop_index
                
            # Push the current bar with its new, furthest-left start index
            stack.append((start, h))
            
        # Cleanup: Any bars left in the stack can extend to the very end of the histogram
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        # Complexity Analysis
        # Time Complexity O(N): Each bar is pushed and popped at most once, leading to a linear time complexity. Inner while loop only runs a max of N times across the entire algorithm
        # Space Complexity O(N): In the worst case, if the heights are in increasing order, we will push all of them onto the stack `stack`
        return max_area