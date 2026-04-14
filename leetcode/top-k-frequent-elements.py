# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return `nums` array itself if size is 1, which is always frequent
        if len(nums) == 1:
            return nums

        # Store each digit in `d` to reference and increment number of times digit appears in `nums`
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        # Sort dictionary values from most to least frequent and return `k` items
        # Complexity Analysis
        # Time Complexity O(N log N): Iterate through `nums` array N times, where N is length of `nums`
        #                             For every number, we use sorted() which takes O(N log N) time
        # Space Complexity O(N): Worst-case is when every number in `nums` is unique, meaning that `d`
        #                        will grow to store N distinct key-value pairs
        #                        Memory scales linearly given a new sorted list of size N in memory
        return sorted(d, key=d.get, reverse=True)[:k]


    def topKFrequentOptimized(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build the frequency map manually
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Step 2: Initialize buckets
        # We create an array of empty lists where the index = frequency.
        # The max frequency is len(nums), so we need size len(nums) + 1.
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        # Group numbers by their frequency
        for num, freq in count.items():
            freq_buckets[freq].append(num)
            
        # Step 3: Gather the top k frequent elements
        ans = []
        
        # Iterate backwards (from highest possible frequency down to 1)
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                ans.append(num)
                # Early exit once we have collected k elements
                if len(ans) == k:
                    return ans
                    
        # Complexity Analysis
        # Time Complexity O(N): Building frequency dictionary and placing elements into bucket array both take O(N) time
        #                       Iterating backwards through buckets array takes O(N) time
        #                       All operations are linear and sequential, resulting in overall time complexity of O(3N) = O(N) by asymptotic law
        # Space Complexity O(N): Worst-case is when every number is unique, our dictionary will store N key-value pairs
        #                        `freq_buckets` array requires N + 1 slots in memory, containing a total of N elements across its sub-lists
        #                        Memory scales linearly with input size
        return ans