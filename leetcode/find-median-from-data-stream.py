# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps to store the data stream.
        # small_heap is a Max-Heap (simulated by multiplying values by -1)
        self.small_heap = []
        # large_heap is a Min-Heap
        self.large_heap = []

    def addNum(self, num: int) -> None:
        # 1. By default, push everything into the small_heap first.
        # (Multiply by -1 to simulate Max-Heap behavior)
        heapq.heappush(self.small_heap, -num)
        
        # 2. Enforce the Value Order: Every number in small_heap MUST be 
        # <= every number in large_heap. If the top of small_heap is greater 
        # than the top of large_heap, we must move it over.
        if (self.small_heap and self.large_heap and 
            (-self.small_heap[0] > self.large_heap[0])):
            highest_of_smalls = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, highest_of_smalls)
            
        # 3. Enforce the Size Balance: The sizes must be equal, OR small_heap 
        # can be exactly 1 element larger.
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        elif len(self.large_heap) > len(self.small_heap):
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -val)

    def findMedian(self) -> float:
        # If lengths are unequal, small_heap has the extra element
        if len(self.small_heap) > len(self.large_heap):
            return float(-self.small_heap[0])
            
        # If lengths are equal, median is the average of both tops
        return (-self.small_heap[0] + self.large_heap[0]) / 2.0
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()