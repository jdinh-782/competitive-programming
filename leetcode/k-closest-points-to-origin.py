# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            # Calculate the squared Euclidean distance
            dist = (x ** 2) + (y ** 2)
            
            # Python has no Max-Heap, so we push negative distances.
            # We store a tuple of (-distance, [x, y]) so the heap can 
            # sort by distance while keeping track of the original point.
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # If our heap exceeds size K, pop the largest distance (the root).
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # The heap now contains the K closest points. 
        # We just need to extract the coordinates from our tuples.

        # Complexity Analysis
        # Time Complexity O(N log K): Process all N points in a single pass. For each point, pushing to the heap and potentially popping
        #                             from the heap takes O(log K) time because the heap's size is strictly capped at K
        # Space Complexity O(K): Memory is dictated by the max size of the heap. Because we continuously pop elements to maintain the
        #                        bounds, our auxiliary space never exceeds O(K)
        return [point for _, point in max_heap]