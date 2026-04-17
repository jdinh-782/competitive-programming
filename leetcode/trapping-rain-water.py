# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def trap(self, height: List[int]) -> int:
        # Begin and End must be a number greater than 0
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            if height[left] == 0:
                left += 1
            
            if height[right] == 0:
                right -= 1

            if height[left] and height[right] > 0:
                break
        
        while left < right:
            if height[right - 1] < height[right]:
                pass
            
            if height[left + 1] < height[left]:
                pass

            left += 1
            right -= 1

        # Complexity Analysis
        # Time Complexity O(N): The `left` and `right` pointers move towards each other until they meet. Even with two
        #                       separate while loops, no element is visited more than once, keeping execution time linear
        # Space Complexity O(1): Only using integer variables to track indices
        return ans

    
    def trapOptimized(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        # Track the tallest walls seen so far from both directions
        max_left = height[left]
        max_right = height[right]
        
        ans = 0
        
        while left < right:
            # We are bottlenecked by the left side
            if max_left < max_right:
                left += 1
                # Update the max wall, or calculate trapped water
                max_left = max(max_left, height[left])
                ans += max_left - height[left]
                
            # We are bottlenecked by the right side
            else:
                right -= 1
                # Update the max wall, or calculate trapped water
                max_right = max(max_right, height[right])
                ans += max_right - height[right]
                
        # Complexity Analysis
        # Time Complexity O(N): The `left` and `right` pointers move towards each other until they meet. Even with two
        #                       separate while loops, no element is visited more than once, keeping execution time linear
        # Space Complexity O(1): Only using integer variables to track indices and results
        return ans