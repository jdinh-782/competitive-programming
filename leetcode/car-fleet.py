# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Note: Assume len(position) = len(speed)
        if len(position) < 2:
            return len(position)
        
        s = []
        ans = 0
        N = len(position)

        for i in range(N):
            meet = position[i] + speed[i]
            # meet = 0 + 4 = 4
            # meet = 2 + 2 = 4
            # meet = 4 + 1 = 5

            if s and s[-1] != meet:
                s = []
                ans += 1
            # ans = 0
            # ans = 0
            # ans = 0 + 1 = 1

            s.append(meet)
            # s = [4]
            # s = [4, 4]
            # s = [5]

        # Last check for remaining elements in s
        if s:
            ans += 1

        # Complexity Analysis
        # Time Complexity O(N): We iterate through the list of cars once, where N is the number of cars
        # Space Complexity O(N): In the worst case, if all cars have different meet times, we will store all of them in the stack `s`
        return ans


    def carFleetOptimized(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions and speeds, then sort by position in descending order
        # (Evaluating cars closest to the target first)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, spd in cars:
            # Calculate time to reach target (can be a float)
            time_to_target = (target - pos) / spd
            # time_to_target = (12 - 10) / 2 = 1
            # time_to_target = (12 - 8) / 4 = 1
            # time_to_target = (12 - 5) / 1 = 7
            # time_to_target = (12 - 3) / 3 = 3
            # time_to_target = (12 - 0) / 1 = 12

            stack.append(time_to_target)
            # stack = [1]
            # stack = [1, 1]
            # stack = [1, 7]
            # stack = [1, 7, 3]
            # stack = [1, 7, 12]
            
            # If the car behind takes LESS OR EQUAL time than the car ahead, they collide!
            # stack[-1] is the car we just added (behind)
            # stack[-2] is the fleet ahead of it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # The faster car behind joins the fleet of the slower car ahead.
                # Pop it so the slower time represents the entire merged fleet.
                stack.pop()
                # stack = [1]
                # stack = [1, 7]
                
        # The size of the stack represents the number of independent fleets

        # Complexity Analysis
        # Time Complexity O(N log N): Sorting the cars takes O(N log N) time, and the subsequent loop runs in O(N) time, leading to an overall time complexity of O(N log N)
        # Space Complexity O(N): In the worst case, if all cars have different times to reach the target, we will store all of them in the stack `stack`
        return len(stack)