# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Note: Last day (element) is always 0
        ans = [0] * len(temperatures)
        s = []

        # Iterate through `temperatures` and keep record of each temp
        for i in range(len(temperatures)):
            temp = temperatures[i]

            # Compare previously stored temp with current, while removing latest < current
            while s and s[-1][0] < temp:
                # Difference in indices lets us know how many days
                diff_ind = i - s[-1][1]
                ans[s[-1][1]] = diff_ind
                s.pop()
            
            s.append((temp, i))
        
        # Complexity Analysis
        # Time COmplexity O(N): Outer for loop is O(N) and inner while loop is O(N) in the worst case, but since each element is pushed and popped at most once, the overall time complexity is O(N)
        # Space Complexity O(N): In the worst case, if the temperatures are in decreasing order, we will push all of them onto the stack `s`
        return ans


    def dailyTemperaturesOptimized(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        # Stack will only store indices, not tuples
        stack = []

        for i, current_temp in enumerate(temperatures):
            # While stack is not empty AND current temp is strictly warmer than the temp at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                # Pop the index of the colder day
                prev_index = stack.pop()
                # Calculate the difference in days
                ans[prev_index] = i - prev_index
                
            # Add the current day's index to the stack
            stack.append(i)
        
        # Complexity Analysis
        # Time Complexity O(N): Each index is pushed and popped at most once, leading to a linear time complexity
        # Space Complexity O(N): In the worst case, if the temperatures are in decreasing order, we will push all indices onto the stack `stack`
        return ans