# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 1. Multiply all stones by -1 to simulate a Max-Heap
        for i in range(len(stones)):
            stones[i] *= -1
            
        # 2. Transform the list into a valid heap in-place in O(N) time
        heapq.heapify(stones)
        
        # 3. Process the stones until 1 or 0 remain
        while len(stones) > 1:
            # Pop the two largest stones (most negative numbers)
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            
            # If they are not equal, push the difference back.
            # (Note: Since they are negative, stone_1 is the "larger" absolute weight. 
            # stone_1 - stone_2 will result in the correct negative remaining weight)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)
                
        # 4. If a stone is left, return its positive value. Otherwise, return 0.

        # Complexity Analysis
        # Time Complexity O(N log N): Multiply by -1 and calling `heapify` takes O(N) time. Worst-case scenario is
        #                             when every smash leaves a remainder, we perform N - 1 iterations. Inside the
        #                             loop, we perform two pops and one push. Each heap operation takes O(log N) time
        # Space Complexity O(1): By mutating the values directly and running `heapify` on the existing `stones` array, we
        #                        avoid allocating any secondary data structures
        return -stones[0] if stones else 0