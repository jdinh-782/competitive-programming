# Name: Johnson Dinh
# Time: 10:26
# Language: Python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        # Exit early if only one digit exists and it equals to target
        if len(nums) == 1 and nums[0] == target:
            return [0]

        # Iterate through the array twice using an explicit method to read through every digit possible
        N = len(nums)
        for i in range(0, N):
            for j in range(0, N):
                if i != j:
                    result = nums[i] + nums[j]
                    if result == target:
                        return [i, j]
        
        # Complexity Analysis
        # Time Complexity O(N^2): Nested loop with both `i` and `j` iterates through entire `num` array of size N, therefore code performs roughly N x N operations
        #                         As input array grows, the execution time increases quadratically
        # Space Complexity O(1): Storing a few integer variables such as `N` and `result` requires a constant amount of space regardless of how large input array gets
        return []


        def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:
            if len(nums) == 0:
                return []
            
            # Exit early if only one digit exists and it equals to target
            if len(nums) == 1 and nums[0] == target:
                return [0]

            # Bypass nested loops and use a hash map to capture numbers we have seen along with their indices
            # Logic relies on algebra that if x + y = target, then y = target - x
            seen = {}
            for i, num in enumerate(nums):
                # y = target - x
                complement = target - num
                
                # Check if y exists in `seen`, then must be complement of x
                if complement in seen:
                    return [seen[complement], i]
                
                seen[num] = i
                
            # Complexity Analysis
            # Time Complexity O(N): Iterate through `nums` array at most one time. Dictionary lookups and insertions in Python run in O(1) constant time
            #                       Overall complexity scales linearly with size of input array
            # Space Complexity O(N): Worst case is when valid pair consists of the last two elements in array which at this point, we would end up storing all N elements inside `seen`
            return []