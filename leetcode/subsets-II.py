# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        # 1. Sort the array so duplicates are adjacent
        nums.sort()
        
        # 2. Define the backtracking helper function
        def backtrack(index: int, current_subset: list[int]):
            # Every time the function is called, the current_subset is valid.
            # Append a deep copy [:] of the current subset to our results.
            res.append(current_subset[:])
            
            # Iterate through all remaining elements to branch out
            for i in range(index, len(nums)):
                # PRUNING STEP: 
                # If we are looking at a duplicate element at the same depth level, skip it.
                if i > index and nums[i] == nums[i-1]:
                    continue
                    
                # 1. Choose: Include the current element
                current_subset.append(nums[i])
                
                # 2. Explore: Recurse on the remaining elements
                backtrack(i + 1, current_subset)
                
                # 3. Un-choose (Backtrack): Remove the element to explore the next branch
                current_subset.pop()

        # 3. Kick off the recursion from index 0 with an empty subset
        backtrack(0, [])
        
        # Complexity Analysis
        # Time Complexity O(N * 2^N): Sorting takes O(N log N) time. In the absolute worst-case scenario, all elements
        #                             are perfectly unique, so the algorithm must generate 2^N subsets. For each valid
        #                             subset, creating a deep copy (`current_subset[:]`) to append to our results takes
        #                             O(N) time. Therefore, the upper bound is mathematically strictly O(N * 2^N)
        # Space Complexity O(N): Memory footprint is dictated entirely by max depth of the system's recursive call stack
        #                        and our `current_subset` tracking array. Because the recursion only goes N levels deep,
        #                        space scales linearly to O(N)
        return res