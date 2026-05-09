# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        # Helper function for DFS backtracking
        def backtrack(current_path: list[int], visited: set[int]):
            # Base Case: if the path length equals nums length, we have a full permutation
            if len(current_path) == len(nums):
                res.append(current_path[:]) # Append a deep copy!
                return
            
            # Try adding every number from the input array
            for num in nums:
                # Eager Pruning: Only proceed if we haven't used this number yet
                if num not in visited:
                    # 1. Choose: Add the number to our path and mark it as visited
                    visited.add(num)
                    current_path.append(num)
                    
                    # 2. Explore: Recurse to pick the next numbers
                    backtrack(current_path, visited)
                    
                    # 3. Un-choose (Backtrack): Remove the number to try the next valid choice
                    current_path.pop()
                    visited.remove(num)
                    
        # Kick off the recursion with an empty path and an empty visited set
        backtrack([], set())
        
        # Complexity Analysis
        # Time Complexity O(N * N!): Mathematical upper bound of possible permutations for N distinct elements is N!. For each
        #                            each of these valid permutations, we hit our base case and execute a deep copy of the array,
        #                            which takes O(N) time
        # Space Complexity O(N): Auxiliary memory footprint is incredibly lightweight. It is comnpletely dictated by the max depth
        #                        of the system's recursive call stack, the `current_path` array, and the `visited` hash set. Because
        #                        the recursion only goes exactly N levels deep before returning, the auxiliary space scales linearly to O(N)
        return res