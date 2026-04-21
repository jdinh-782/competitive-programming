# Name: Johnson Dinh
# Time: 21:01
# Language: Python3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                s.append(token)
            else:
                # Assume that `s` contains at least 2 elements to perform operation on
                val1 = int(s.pop())
                val2 = int(s.pop())

                if token == '+':
                    s.append(val2 + val1)
                elif token == '-':
                    s.append(val2 - val1)
                elif token == '*':
                    s.append(val2 * val1)
                elif token == '/':
                    s.append(val2 / val1)

        # Complexity Analysis
        # Time Complexity O(N): Iterate through `tokens` once to check each token if it's an operator or operand. Each operation (push and pop) is O(1)
        # Space Complexity O(N): In the worst case, if all tokens are operands, we will push all of them onto the stack `s`
        return int(s[0])