# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # 1. If the sum is odd, it cannot be partitioned evenly
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # 2. DP set to store all possible sums we can generate
        dp = set([0])
        
        # 3. Iterate through each number
        for num in nums:
            next_dp = set()
            
            for t in dp:
                new_sum = t + num
                
                # 4. Early Exit: If we hit the target exactly, we are done!
                if new_sum == target:
                    return True
                
                # We only care about sums that are less than the target.
                # Anything larger is useless and bloats memory.
                if new_sum < target:
                    next_dp.add(new_sum)
                    
                # Add the original sum (representing the choice to NOT include 'num')
                next_dp.add(t)
                
            dp = next_dp
        
        # Complexity Analysis
        # Time Complexity O(N x T): We iterate through all N numbers. In the worst-case scenario, our `dp` set could become perfectly dense, containing every single integer from 0 up to T. Therefore, 
        #                           the inner loop runs at most T times. Because the time scales based on the numeric value of the target rather than just the input size, this is known as a 
        #                           pseudo-polynomial time complexity
        # Space Complexity O(T): Max number of elements our `dp` and `next_dp` Hash Sets will ever hold is bounded exactly by the `target` value, because we actively discard any sums greater than
        #                        the target (`if new_sum < target`)
        return False