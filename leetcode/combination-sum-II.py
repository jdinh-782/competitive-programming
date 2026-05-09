# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # 1. Sort the array to enable adjacent duplicate checking and early stopping
        candidates.sort()
        res = []
        
        # 2. Define the backtracking helper function
        def backtrack(start_index: int, target_remain: int, current_path: list[int]):
            # Base Case 1: We hit our exact target
            if target_remain == 0:
                res.append(current_path[:])
                return
                
            # Iterate through remaining candidates
            for i in range(start_index, len(candidates)):
                # PRUNING 1: Skip duplicate elements at the same depth level
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                
                # PRUNING 2: Early stopping. 
                # If this number is too big, subsequent numbers are also too big.
                if target_remain - candidates[i] < 0:
                    break
                    
                # 1. Choose: Include the candidate
                current_path.append(candidates[i])
                
                # 2. Explore: Recurse with updated target and next index (i + 1)
                # Note: It's i + 1 because we can only use each number once!
                backtrack(i + 1, target_remain - candidates[i], current_path)
                
                # 3. Un-choose (Backtrack): Remove the candidate
                current_path.pop()

        # 3. Kick off recursion
        backtrack(0, target, [])

        # Complexity Analysis
        # Time Complexity O(2^N): Sorting takes O(N log N) time. In the absolute worst-case scenario, all elements are unique
        #                         and the target is massive, the algorithm must explore an exponential state-space tree,
        #                         yielding 2^N potential combinations. For each valid path, creating a deep copy (`current_path[:]`)
        #                         to append to our results takes O(N) time. Therefore, the strict mathematical upperr bound is
        #                         O(N * 2^N). However, because of the dual-pruning strategy, the actual execution time drops
        # Space Complexity O(N): Auxiliary memory footprint is dictated by the max depth of the system's recursive call stack and
        #                        our `current_path` tracking array. Because the recursion can never go deeper than N levels, the
        #                        auxiliary space scales strictly linearly to O(N)
        return res