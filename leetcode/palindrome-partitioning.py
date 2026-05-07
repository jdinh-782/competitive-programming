# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        current_partition = []
        
        # Helper function to check if a string is a palindrome
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # DFS Backtracking function
        def backtrack(start_index: int):
            # Base Case: If we've reached the end of the string, 
            # we've found a valid complete partition.
            if start_index >= len(s):
                res.append(current_partition[:]) # Append a copy!
                return
            
            # Try every possible end index for the current substring
            for end_index in range(start_index, len(s)):
                # If the current prefix is a palindrome, we can proceed
                if is_palindrome(start_index, end_index):
                    # 1. Choose: Add the palindrome substring
                    current_partition.append(s[start_index : end_index + 1])
                    
                    # 2. Explore: Recurse on the remaining part of the string
                    backtrack(end_index + 1)
                    
                    # 3. Un-choose (Backtrack): Remove the substring to try the next split
                    current_partition.pop()

        # Kick off the recursion from the beginning of the string
        backtrack(0)

        # Complexity Analysis
        # Time Complexity O(N * 2^N): In the absolute worst-case scenario, every single character in the string is
        #                             identical. A string of length N has N - 1 potential cut points between
        #                             characters. Each cut point can either be included or excluded, leading to 2^(N-1)
        #                             total valid partitions. For each successful partition, it takes O(N) time to deep
        #                             copy the substrings into the final `res` array
        # Space Complexity O(N): Memory footprint is entirely dictated by the max depth of the system's recurisve call
        #                        stack and our `current_partition` state array. In the worst case, we will need to make
        #                        a cut after every single character, the recursion goes exactly N levels deep
        return res