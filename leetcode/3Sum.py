# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Base case if only 3 digits exist, then we only need to compare these 3 digits since each digit can only be used once
        if len(nums) == 3:
            if (nums[0] + nums[1] + nums[2]) == 0:
                return [nums]
            return []
    

        # Iterate through the array with 3 indices, starting from 0
        # Decrement j and k as we go through the array while comparing the sums from 3 digits with different indices
        N = len(nums)
        i = 0
        j = N - 1
        k = j - 1
        results = list()

        while i < N:
            # -1 + (-4) + (-1) = -6     i = 0, j = 5, k = 4
            # -1 + (-4) + 2 = -3        i = 0, j = 5, k = 3
            # -1 + (-4) + 1 = -4        i = 0, j = 5, k = 2
            # -1 + (-4) + 0 = -5        i = 0, j = 5, k = 1

            # -1 + (-1) + 2 = 0         i = 0, j = 4, k = 3        [-1, -1, 2]
            # -1 + (-1) + 1 = -1        i = 0, j = 4, k = 2
            # -1 + (-1) + 0 = -2        i = 0, j = 4, k = 1

            # -1 + 2 + 1 = 2            i = 0, j = 3, k = 2
            # -1 + 2 + 0 = 1            i = 0, j = 3, k = 1

            # -1 + 1 + 0 = 0            i = 0, j = 2, k = 1        [-1, 1, 0]
            if (i != j) and (i != k) and (j != k):
                num1 = nums[i]
                num2 = nums[j]
                num3 = nums[k]
                ans = num1 + num2 + num3
                result = [num1, num2, num3]

                if ans == 0 and result not in results:
                    results.append(result)

            k -= 1

            if k == 0:
                j -= 1
                k = j - 1

            if j == 1:
                i += 1
                j = N - 1
                k = j - 1

        # Complexity Analysis
        # Time Complexity O(N^3): Logic essentially checks almost every possible triplet combination of `i`, `j`, and `k`. Thus, algorithm
        #                         scales cubically and checking if `result` is not in `results` array runs in O(M) linear scan each time
        #                         a valid tripletn is found
        # Space Complexity O(1): In auxiliary space, we only store contents in the `results` array which is O(1) for inserts. All other
        #                        variable assignments are O(1)
        return results



    def threeSumOptimized(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to easily handle duplicates and enable two-pointer math
        nums.sort()
        results = []
        N = len(nums)
        
        for i in range(N - 2):
            # If the fixed number is > 0, the sum can never be 0 since the array is sorted
            if nums[i] > 0:
                break
                
            # Skip adjacent duplicates for the fixed pointer 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two-Pointer setup for the remainder of the array
            left = i + 1
            right = N - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    # Sum is too small, move left pointer right to a bigger number
                    left += 1
                elif current_sum > 0:
                    # Sum is too big, move right pointer left to a smaller number
                    right -= 1
                else:
                    # We found a valid triplet!
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers inward to keep looking for other combinations
                    left += 1
                    right -= 1
                    
                    # Skip adjacent duplicates for the 'left' pointer to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        # Complexity Analysis
        # Time Complexity O(N^2): Sorting the array initially takes O(N log N) time and since we only utilize one for loop, this
        #                         takes O(N) time for only one traversal throughout the array. Inside of the loop, the `left` and
        #                         `right` pointers traverse inward which take O(N) time per iteration separately. Therefore, the
        #                         overall time complexity is O(N log N) + O(N^2) -> O(N^2)
        # Space Complexity O(N): In auxiliary space, the memory footprint is assuming that sort() is using Timsort, which assumes
        #                        O(N) time. Storing the results only occur in O(1) insertion time
        return results