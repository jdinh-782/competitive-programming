# Name: Johnson Dinh
# Time: 6:01
# Language: Python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Two pointers to keep track of each element's index from both ends of the list
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Check if nums[left] or nums[right] is already target
            if nums[left] == target:
                return left
            
            if nums[right] == target:
                return right

            # Find the midpoint index of where the pointers are currently standing
            mid = (left + right) // 2

            # Analyze midpoint element to determine if we should increment or decrement pointers
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # Complexity Analysis
        # Time Complexity: O(log n) where n is the length of the input list. This is because we are halving the search space with each iteration
        # Space Complexity: O(1) since we are using only a constant amount of extra space for the pointers and variables
        return -1