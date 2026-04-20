# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        begin = 0
        end = len(s) - 1
        result = False
        while begin < end:
            if s[begin] in pairs and pairs[s[begin]] == s[end]:
                result = True
            else:
                result = False

            begin += 1
            end -= 1

        # Complexity Analysis
        # Time Complexity O(N): Where N is the length of the input string s. We traverse the string once
        # Space Complexity O(1): We are only storing a fixed-size dictionary of pairs and two integer pointers which result in constant time
        return result
        

    def isValidOptimized(self, s: str) -> bool:
        # Base case: an odd length string can never be perfectly matched
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # Mapping closing brackets to their respective opening brackets
        # This makes the lookup process much cleaner
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop the top element if the stack isn't empty, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the required opening bracket, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched. If not, it's invalid.

        # Complexity Analysis
        # Time Complexity O(N): Where N is the length of the input string s. We traverse the string once
        # Space Complexity O(N): In the worst case if all characters are opening brackets and we push them onto the stack
        #                        In the best case, if the string is perfectly matched, the space complexity would be O(1) as the stack would be empty at the end
        return not stack