# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = min(piles)
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2

            k = mid // h
            if k == 0:
                return k

            if mid < h:
                right = mid - 1
            else:
                left = mid + 1

        # Complexity Analysis
        # Time Complexity O(log N): Where N is the difference between the maximum and minimum pile size. This is because we are halving the search space with each iteration
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return left


    def minEatingSpeedOptimized(self, piles: list[int], h: int) -> int:
        # Minimum possible speed is 1, maximum is the largest pile
        left = 1
        right = max(piles)
        
        # Keep track of the minimum valid speed found so far
        best_speed = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Calculate total hours to eat all piles at speed 'mid'
            total_hours = 0
            for p in piles:
                # Equivalent to math.ceil(p / mid) but using integer math
                total_hours += (p + mid - 1) // mid
                
            # If Koko can finish within h hours, this speed is valid.
            # Record it, and try to find an even slower (smaller) valid speed.
            if total_hours <= h:
                best_speed = mid
                right = mid - 1
            else:
                # Koko took too long. She must eat faster.
                left = mid + 1
        
        # Complexity Analysis
        # Time Complexity O(N log M): Where N is the number of piles and M is the maximum pile size. This is because we are performing a binary search on the range of 
        #                             possible speeds (which is at most M) and for each speed, we calculate the total hours which takes O(N) time
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return best_speed