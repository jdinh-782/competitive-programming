# Name: Johnson Dinh
# Time: 8:53
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        curr = head
        seen = []

        while curr.next is not None:
            if curr not in seen:
                seen.append(curr)
            
            if curr.next in seen:
                return True

            curr = curr.next
        
        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of nodes in the linked list. In the worst case, we will traverse all nodes once, 
        #                       resulting in O(N) time complexity. However, if there is a cycle, we may encounter a node that we've 
        #                       already seen before, which would allow us to return early
        # Space Complexity O(N): In the worst case, if there is no cycle, we will store a reference to each node in the 'seen' list, 
        #                        resulting in O(N) space complexity. If there is a cycle, we may store fewer nodes before we encounter 
        #                        a duplicate, but in the worst case, we could still end up storing all nodes before detecting the cycle
        return False

    
    def hasCycleOptimized(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, it can't have a cycle
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Fast moves 2 steps, so we must check fast and fast.next are not None
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they meet, there is a cycle
            if slow == fast:
                return True
                

        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of nodes in the linked list. In the worst case, we will traverse all nodes once, 
        #                       resulting in O(N) time complexity. If there is a cycle, we will eventually encounter a node that we've 
        #                       already seen before, which would allow us to return early
        # Space Complexity O(1): We are using only constant space to store the pointers slow and fast, regardless of the size of the linked 
        #                        list. We are not using any additional data structures that grow with the input size, so the space complexity is O(1)
        return False