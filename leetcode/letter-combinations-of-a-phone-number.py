# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Edge case: If the input is empty, return an empty list immediately.
        if not digits:
            return []
            
        # 1. Create the T9 mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        # 2. Define the backtracking helper function
        def backtrack(index: int, current_string: str):
            # Base Case: If the length of the string matches the digits length
            if index == len(digits):
                res.append(current_string)
                return
                
            # Recursive Step: Get the letters for the current digit
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]
            
            # Loop through each possible letter and branch out
            for letter in possible_letters:
                # Move to the next digit (index + 1) and append the letter
                backtrack(index + 1, current_string + letter)
                
        # 3. Kick off the recursion from index 0 with an empty string
        backtrack(0, "")
        
        # Complexity Analysis
        # Time Complexity O(4^N * N): In the absolute worst-case scenario, the user inputs digits that all map
        #                             to 4 letters. For N digits, the decision tree will have a maximum of 4^N leaf
        #                             nodes (combinations). Furthermore, at each leaf node, creating the final string
        #                             and appending it to our results array takes O(N) time
        # Space Complexity O(N): Memory footprint is entirely dictated by the max depth of the system's call stack. Because
        #                        we process one complete combination at a time, the recursion only ever goes exactly N
        #                        levels deep before hitting the base case and returning
        return res