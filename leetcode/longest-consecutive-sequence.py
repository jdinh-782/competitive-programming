# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        # Create a new list of unique nums
        unique_nums = list(set(nums))

        # Sort elements from smallest to largest
        unique_nums.sort()

        max_result = 1  # Store the max length from analyzing each sequence
        result = 1      # Store the length of individual sequence
        val = unique_nums[0]

        # Iterate through all nums and calculate next acceptable digit in sequence
        for i in range(1, len(unique_nums)):
            next_val = val + 1

            if unique_nums[i] == next_val:
                val = next_val
                result += 1
            else:
                # Store length of current sequence if result is higher than previous
                if result > max_result:
                    max_result = result

                # Reset sequence count if current number is not accepted
                val = unique_nums[i]
                result = 1
        
        # Store length of current sequence if result is higher than previous
        if result > max_result:
            max_result = result
        
        # Complexity Analysis
        # Time Complexity O(N log N): Using sort() causes solution to bottleneck since this algorithm runs in O(N log N) time. Converrting list to
        #                             a set along with for loop both take O(N) time, however, sorting algorithm overrides time complexity
        # Space Complexity O(N): Creating a list for `unique_nums` to store elements, worst case is when all numbers are unique. Algorithm scales
        #                        linearly with the input size
        return max_result
    

    def longestConsecutiveOptimized(self, nums: List[int]) -> int:
        # Convert to a set for O(1) lookups
        num_set = set(nums)
        max_sequence = 0
        
        for num in num_set:
            # Check if this number is the start of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_sequence = 1
                
                # For every number in set, check if (num - 1) exists in the set
                # if (num - 1) DOES exist, then the current number is NOT the beginning of a sequence, so we move on
                # if (num - 1) DOES NOT exist, then the current number must be start of a sequence

                # If we are at start of a sequence, then use while loop to count upwards by 1 and measure the length of the specific sequence
                # Count upwards as long as the next consecutive number exists
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_sequence += 1
                    
                # Update the maximum sequence length found so far
                if current_sequence > max_sequence:
                    max_sequence = current_sequence
        
        # Complexity Analysis
        # Time Complexity O(N): Although there is a while loop within a for loop, we are only checking if (num - 1) is not in the set, therefore
        #                       we need only to run the inner while loop when we find the beginning of a sequence. Due to this, a number can only
        #                       be visited inside that while loop exactly once. Every number in the array is processed at most twice (once by the
        #                       outer for loop, once by the inner while loop)
        # Space Complexity O(N): We need to allocate a brand new hash set to store the unique elements. Worst case is where every element in the
        #                        array is completely unique, which will cause the set to grow store all N elements, meaning that memory scales linearly
        return max_sequence