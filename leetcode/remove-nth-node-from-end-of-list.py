# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = -1
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            i += 1

        ind = n + i
        i = 0
        curr = head
        prev = None

        while curr:
            if i == ind and prev:
                prev.next = curr.next
                curr.next = None
                curr.val = 0
                return head
            
            prev = curr
            curr = curr.next
            i += 1

        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of nodes in the linked list. The first while loop traverses the list to find the 
        #                       middle, which takes O(N/2) time. The second while loop traverses the list again to find the node to 
        #                       remove, which also takes O(N/2) time. Therefore, the overall time complexity is O(N/2 + N/2) = O(N)
        # Space Complexity O(1): We are using only constant space to store the pointers slow, fast, curr and prev, as well as the 
        #                        integer variables i and ind. We are not using any additional data structures that grow with the 
        #                        input size, so the space complexity is O(1)
        return None


    def removeNthFromEndOptimized(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node pointing to the head.
        # This handles the edge case where the head itself needs to be removed.
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = head
        
        # Step 2: Move 'fast' exactly 'n' steps ahead to create the gap
        for _ in range(n):
            fast = fast.next
            
        # Step 3: Move both pointers at the same speed until 'fast' reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Step 4: 'slow' is now resting on the node exactly BEFORE the target node.
        # Sever the target node by skipping over it.
        slow.next = slow.next.next
        
        # Return the new head (which handles the case if the original head was removed)
        return dummy.next