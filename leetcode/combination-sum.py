# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        # Optional Optimization: Sorting allows us to break out of loops early
        candidates.sort()
        
        def backtrack(start_index: int, target_remain: int, current_path: list[int]):
            # Base Case 1: We hit our exact target
            if target_remain == 0:
                res.append(current_path[:])
                return
            
            # Iterate through the candidates, starting strictly at the start_index
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # PRUNING (Early Stopping): Because the array is sorted, 
                # if this candidate exceeds the target, all subsequent ones will too.
                if target_remain - candidate < 0:
                    break 
                
                # 1. Choose: Add the candidate to our path
                current_path.append(candidate)
                
                # 2. Explore: Recurse with the updated target. 
                # Note: We pass 'i' (not i+1) to allow unlimited reuse of the same number!
                backtrack(i, target_remain - candidate, current_path)
                
                # 3. Un-choose (Backtrack): Remove the candidate to try the next one
                current_path.pop()

        # Kick off the recursion from index 0
        backtrack(0, target, [])

        # Complexity Analysis
        # Time Complexity O(N^(T/M)): Branching factor of decision tree is bounded by N. Absolute max depth of our recursive tree occurs when
        #                             algorithm repeatedly picks the smallest element in the array (M) until it hits or exceeds the target T,
        #                             resulting in a max depth of T/M
        # Space Complexity O(T/M): Auxiliary memory footprint is dictated by max depth of system's recursive call stack and the `current_path`
        #                          tracking array. Because the recursion can never go deeper than T/M levels, the auxiliary space strictly
        #                          scales to O(T/M)
        return res