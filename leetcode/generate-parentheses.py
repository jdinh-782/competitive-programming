# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        # Helper function for DFS backtracking
        def backtrack(open_count: int, closed_count: int, current_string: str):
            # Base Case: The string is complete when it reaches length 2*n
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # Choice 1: Add an open parenthesis if we haven't hit the limit
            if open_count < n:
                backtrack(open_count + 1, closed_count, current_string + "(")
                
            # Choice 2: Add a closed parenthesis if it can match an open one
            if closed_count < open_count:
                backtrack(open_count, closed_count + 1, current_string + ")")
                
        # Kick off the recursion with 0 open, 0 closed, and an empty string
        backtrack(0, 0, "")
        
        # Complexity Analysis
        # Time Complexity O(4^n/sqrt(n)): Since we perfectly constrain our backtracking to only valid paths, our time
        #                                 complexity rightly hugs the theoretical minimum. The n-th Catalan number dictates
        #                                 the exact number of valid combinations. Building each string takes O(N) time,
        #                                 resulting in an asymptotic time complexity bounded by O(4^n/sqrt(n))
        # Space Complexity O(n): Memory footprint is dictated by max depth of the system's call stack. Because each valid
        #                        string has exactly length 2n, the recursion only ever goes exactly 2n levels deep before
        #                        returning. This simplifies asymptotically to O(n)
        return res