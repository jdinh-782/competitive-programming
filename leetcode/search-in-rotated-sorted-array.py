# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            # Check immediately if nums[left] or nums[right] is the target
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[right]:
                if nums[right] > target:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[right] > target:
                    left = mid + 1
                else:
                    right = mid
        
        # Complexity Analysis
        # Time Complexity O(log N): Where N is the length of the input list. This is because we are halving the search space with each iteration
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return -1


    def searchOptimized(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
                
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                
            # 1. Is the Left Half sorted?
            if nums[left] <= nums[mid]:
                # Is the target mathematically inside this sorted Left Half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is here, discard right half
                else:
                    left = mid + 1   # Target is not here, discard left half
                    
            # 2. Otherwise, the Right Half MUST be sorted
            else:
                # Is the target mathematically inside this sorted Right Half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is here, discard left half
                else:
                    right = mid - 1  # Target is not here, discard right half
        
        # Complexity Analysis
        # Time Complexity O(log N): Where N is the length of the input list. This is because we are halving the search space with each iteration
        # Space Complexity O(1): Since we are using only a constant amount of extra space for the pointers and variables
        return -1