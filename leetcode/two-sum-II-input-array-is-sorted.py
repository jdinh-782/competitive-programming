# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Base case: If only 2 elements are provided and tests are generated to have exactly one solution,
        #            then the result must be the 2 indices
        if len(numbers) == 2:
            return [1, 2]
        
        # Method using pointers
        end = len(numbers)
        i = 0

        # Since numbers is already sorted, no point in looking at last element since we already found the sums from previous iterations
        while i < (end - 1):
            j = i + 1

            # Iterate from j to the end to see if remaining elements sum to target
            while j < end:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j += 1
            
            i += 1
        
        # Complexity Analysis
        # Time Complexity O(N^2): Due to a nested while loop and the certainty that the array is being iterated again, the time complexity
        #                  is O(N^2) since we are iterating in both the outer and inner while loops
        # Space Complexity O(1): We are only allocating a few variables such as `i`, `j`, and `end` in our algorithm, so the extra space
        #                        used remains constant regardless of input size
        return [i + 1, j + 1]


    def twoSumOptimized(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the extremes of the array
        left = 0
        right = len(numbers) - 1
        
        # Iterate using the left and right pointers to determine if result is too small or too large
        # Since `numbers` is already sorted, we don't need to worry if the sum is stretched out somewhere else
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem requires 1-indexed answers, so we add 1 to both indices
                return [left + 1, right + 1]
            
            elif current_sum < target:
                # Sum is too small, move the left pointer to a larger number
                left += 1
                
            else:
                # Sum is too large, move the right pointer to a smaller number
                right -= 1

        # Problem guarantees exactly one solution, so no return here

        # Complexity Analysis
        # Time Complexity O(N): Using one loop to iterate through the entire array with a left and right pointer,
        #                       which will meet in the exact middle of the array
        # Space Complexity O(1): In auxiliary space, we only allocate memory for a few integer variables which
        #                        guarantees our memory footprint remains strictly constant