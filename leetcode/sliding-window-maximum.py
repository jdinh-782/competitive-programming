# Name: Johnson Dinh
# Time: 12:45
# Language: Python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        N = len(nums)
        i = 0
        maximum = []

        while i < (N - k + 1):
            window = nums[i:(k+i)]
            maximum.append(max(window))
            i += 1

        # Complexity Analysis
        # Time Complexity O(N * K): We iterate through the array once (N) and for each window of size k, we call max() which takes O(K) time to find the maximum in that window
        # Space Complexity O(N): We are storing the maximum of each window in a list which will have N - K + 1 elements since that is how many windows we can create from the input array
        return maximum


    def maxSlidingWindowOptimized(self, nums: list[int], k: int) -> list[int]:
        # q will store our indices, but we will never use .pop(0) on it
        q = []
        head = 0  # This pointer represents the virtual "front" of our deque
        result = []
        
        for i in range(len(nums)):
            # 1. Remove elements from the left that are no longer in the window
            # Instead of popping, we just advance the head pointer
            if head < len(q) and q[head] < i - k + 1:
                head += 1
                
            # 2. Remove elements from the right that are smaller than the current element
            # We only pop as long as our list length is strictly greater than our head pointer
            while len(q) > head and nums[q[-1]] < nums[i]:
                q.pop()
                
            # 3. Add the current element's index to the right
            q.append(i)
            
            # 4. If our window has reached size k, the maximum is always at our virtual front
            if i >= k - 1:
                result.append(nums[q[head]])
        
        # Complexity Analysis
        # Time Complexity O(N): Each element is added to the deque once and removed at most once, resulting in linear time complexity
        # Space Complexity O(K): The deque will hold at most k indices at any time, since we are only interested in the current window of size k
        #                        The result list will hold N - K + 1 elements, but since we are only returning the result, we consider the space complexity 
        #                        in terms of the deque which is O(K) where K is the size of the sliding window and is independent of N, the length of the input array 
        #                        The result list is not considered in space complexity analysis as it is required for output
        return result