# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = None
        curr = head

        while curr:
            nxt = curr.next
            temp = nxt.next
            curr.next = temp
            temp.next = nxt

            curr = nxt

        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of nodes in the linked list. The while loop traverses each node 
        #                       in the list once, resulting in O(N) time complexity
        # Space Complexity O(1): We are using only constant space to store the pointers temp, curr and nxt. We are 
        #                        not using any additional data structures that grow with the input size, so the space complexity is O(1)


    def reorderListOptimized(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # STEP 1: Find the middle using Slow and Fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # STEP 2: Reverse the second half of the list
        second = slow.next
        slow.next = None # Break the link to separate into two lists
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # STEP 3: Merge the two halves alternately
        first, second = head, prev
        while second:
            # Save next pointers
            tmp1, tmp2 = first.next, second.next
            
            # Link first -> second
            first.next = second
            # Link second -> first's original next
            second.next = tmp1
            
            # Shift pointers forward
            first, second = tmp1, tmp2

        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of nodes in the linked list. Each of the three steps (finding the 
        #                       middle, reversing the second half, and merging) traverses the list at most once, resulting in O(N) time complexity
        # Space Complexity O(1): We are using only constant space to store the pointers slow, fast, prev, tmp, tmp1 
        #                        and tmp2. We are not using any additional data structures that grow with the input size, so the space complexity is O(1)