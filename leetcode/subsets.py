# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        # Define the backtracking helper function
        def backtrack(start_index: int, current_subset: list[int]):
            # Every node we visit is a valid subset. 
            # We must append a deep copy [:] of the current subset.
            res.append(current_subset[:])
            
            # Iterate through the remaining elements to branch out
            for i in range(start_index, len(nums)):
                # 1. Choose: Include the current element
                current_subset.append(nums[i])
                
                # 2. Explore: Recurse on the remaining elements (i + 1)
                backtrack(i + 1, current_subset)
                
                # 3. Un-choose (Backtrack): Remove the element to explore the next branch
                current_subset.pop()

        # Kick off the recursion from index 0 with an empty subset
        backtrack(0, [])
        
        # Complexity Analysis
        # Time Complexity O(N * 2^N): Mathematically, a set of size N has exactly 2^N possible subsets. DFS visits
        #                             exactly 2^N nodes. At every single node, we execute `current_subset[:}`
        # Space Complexity O(N): Auxiliary memory footprint is dictated by the max depth of the system's recursive
        #                        call stack and our mutable `current_subset` tracking array. Because the recursion
        #                        explores a max depth of exactly N levels before returning, the auxiliary space
        #                        strictly scales to O(N)
        return res