# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        
        # 1. Transform the initial array into a valid Min-Heap in O(N) time
        heapq.heapify(self.min_heap)
        
        # 2. Trim the heap down so it only contains the K largest elements.
        # We pop the smallest elements until the size is exactly K.
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # 1. Push the new stream value into the heap
        heapq.heappush(self.min_heap, val)
        
        # 2. If pushing caused us to exceed size K, eject the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # 3. The root of the Min-Heap is always the Kth largest element
        return self.min_heap[0]