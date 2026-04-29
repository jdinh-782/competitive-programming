# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        begin = 0
        end = len(nums) - 1

        while begin < end:
            if nums[begin] == nums[end]:
                return nums[end]

            if nums[begin] > nums[end]:
                begin += 1
            else:
                end -= 1
        
        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of elements in the input array nums. The while loop iterates
        #                       through the array, and in the worst case, it may need to check each element
        #                       once. Therefore, the time complexity is O(N)
        # Space Complexity O(1): We are using only a constant amount of extra space to store the pointers begin 
        #                       and end, as well as a few integer variables. We are not using any additional 
        #                       data structures that grow with the input size, so the space complexity is O(1)
        return nums[end]


    def findDuplicateOptimized(self, nums: list[int]) -> int:
        # Phase 1: Tortoise and Hare find the intersection point
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]           # 1 step
            fast = nums[nums[fast]]     # 2 steps
            
        # Phase 2: Find the entrance to the cycle
        slow = 0 # Reset slow to the start
        
        while slow != fast:
            slow = nums[slow]           # 1 step
            fast = nums[fast]           # 1 step (fast now moves at same speed)
            
        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of elements in the input array nums. The first phase of the 
        #                       algorithm (finding the intersection point) takes O(N) time in the worst case, as 
        #                       the fast pointer can traverse the entire array. The second phase (finding the entrance 
        #                       to the cycle) also takes O(N) time in the worst case, as both pointers may need to 
        #                       traverse the entire array again. Therefore, the overall time complexity is O(N + N) = O(N)
        # Space Complexity O(1): We are using only a constant amount of extra space to store the pointers slow and 
        #                        fast, as well as a few integer variables. We are not using any additional data structures 
        #                        that grow with the input size, so the space complexity is O(1)
        return slow