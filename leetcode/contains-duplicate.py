# Name: Johnson Dinh
# Time: 7:22
# Language: Python3
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        d = {}
        for num in nums:
            # lookup in Python is O(1) on average
            if num not in d:
                # insertion in Python is O(1) on average
                d[num] = 1  
            else:
                d[num] += 1
                if d[num] >= 2:
                    return True

        # Complexity Analysis
        # Time Complexity: Iterating through `nums` array at most one time, assuming at least one lookup and at least one insertion, overall time complexity scales linearly with size of the input array
        # Space Complexity Worst-case (`nums` array has no duplicates) is that `d` will end up storing all N elements as keys, therefore memory used scales linearly with input
        return False


    def containsDuplicateOptimized(self, nums: List[int]) -> bool:
        # Utilize an empty structure (set) to store unique values as keys only since we're only worried about uniqueness
        seen = set()

        # Iterate through `nums` array to check IF a duplicate exists, so do we not need to keep a running count of occurrences
        for num in nums:
            # Early exit if `num` already exists in `seen`
            if num in seen:
                return True

            # Add `num` to `seen` to signify that we "saw" the number
            seen.add(num)

        # Complexity Analysis
        # Time Complexity: Iterating through `nums` array at most one time, assuming at least one lookup and at least one insertion, overall time complexity scales linearly with size of the input array
        # Space Complexity Worst-case (`nums` array has no duplicates) is that `d` will end up storing all N elements as keys, therefore memory used scales linearly with input
        return False