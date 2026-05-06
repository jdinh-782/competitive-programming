# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            # 1. Push the current number into our heap
            heapq.heappush(min_heap, num)
            
            # 2. If our heap exceeds size K, pop the smallest element.
            # This ensures we are only tracking the K *largest* elements.
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # 3. The root of the heap is the smallest of the K largest elements,
        # which is exactly the Kth largest element overall.

        # Complexity Analysis
        # Time Complexity O(N log K): Iterate through all N elements exactly once. For each element, we perform
        #                             a heap push and potentially a heap pop. Because we strictly enforce the heap
        #                             capacity to never exceed K, these operations take at most O(log K) time
        # Space Complexity O(K): Memory is strictly dictated by the max size of the heap. Because we continuously
        #                        pop elements when the size exceeds K, auxiliary space never grows beyond O(K) 
        return min_heap[0]