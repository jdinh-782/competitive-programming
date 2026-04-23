# Name: Johnson Dinh
# Time: 24:36
# Language: Python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            else:
                return nums[1]

        left = 0
        right = len(nums) - 1
        ans = 0

        # At the beginning, if first < last element, then array is already rotated properly
        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            # If number before nums[right] is greater, then nums[right] must be "beginning" of rotated array, i.e. the minimum
            if nums[right - 1] > nums[right]:
                return nums[right]
            else:
                right -= 1

            mid = (left + right) // 2
            
            # If midpoint element > nums[right], all elements before midpoint must be greater than nums[right]
            # Set left pointer to index after midpoint
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                ans = nums[mid]
                right -= 1

        # Complexity Analysis
        # Time Complexity O(log N): Where N is the length of the input list. This is because we are halving the search space with each iteration
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables 
        return ans


    def findMinOptimized(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is strictly greater than the rightmost element,
            # the inflection point (minimum) MUST be to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
                
            # Otherwise, the right half is sorted, meaning the minimum 
            # is either at mid or somewhere to the left of mid.
            else:
                right = mid
                
        # When left == right, we have converged on the minimum element

        # Complexity Analysis
        # Time Complexity O(log N): Where N is the length of the input list. This is because we are halving the search space with each iteration
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return nums[left]