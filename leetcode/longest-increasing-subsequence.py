# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import bisect

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 'sub' will store the smallest tail for all increasing subsequences
        # of length i+1. (e.g., sub[0] is the smallest tail of a length 1 subseq)
        sub = []
        
        for x in nums:
            # Find the index where x can replace a number to create a smaller tail
            # bisect_left uses Binary Search to find this in O(log N) time
            i = bisect.bisect_left(sub, x)
            
            # If x is larger than all elements in sub, it extends the subsequence
            if i == len(sub):
                sub.append(x)
            # Otherwise, overwrite the existing element to lower the tail bound
            else:
                sub[i] = x
                
        # The length of our 'sub' array represents the length of the LIS

        # Complexity Analysis
        # Time Complexity O(N log N): Iterate through the array of N elements exactly once. Inside the loop, we perform a Binary Search (`bisect_left`) on the `sub` tracking array, which takes
        #                             O(log N) time per element. Therefore, the total processing time scales strictly to O(N log N), safely bypassing Time Limit Exceeded errors on massive datasets
        # Space Complexity O(N): Memory footprint is dictated by our `sub` tracking array. Worst-case scenario is when the input array is strictly increasing, like `[1, 2, 3, 4]`, the `sub` array
        #                        will grow to store every single element
        return len(sub)