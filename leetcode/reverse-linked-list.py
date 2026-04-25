# Name: Johnson Dinh
# Time: 3:30
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # curr = head = [1, 2, 3, 4, 5] = 1
        # nxt = 2
        # curr.next = None
        # prev = 1
        # curr = [2, 3, 4, 5, 1] = 2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Complexity Analysis
        # Time Complexity O(N): Let N be number of nodes in linked list. The while loop traverses each single node exactly once
        # Space Complexity O(1): We are using only constant space to store the pointers prev, curr and nxt
        return prev


    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or we reached the last node
        if not head or not head.next:
            return head
            
        # Traverse all the way to the end. 
        # 'new_head' will always be the last node (e.g., 5)
        new_head = self.reverseList(head.next)
        
        # As the call stack pops (unwinds), flip the pointer
        # Example: if head is 4, head.next is 5. 
        # We want 5 to point to 4: head.next.next = head
        head.next.next = head
        
        # Break the old forward link to prevent a cycle
        head.next = None
        
        # Complexity Analysis
        # Time Complexity O(N): Let N be number of nodes in linked list. The recursive function is called once for each node in the list
        # Space Complexity O(N): The space complexity is O(N) because of the recursive call stack. In the worst case, when the linked 
        #                        list is completely unbalanced (e.g., all nodes are in a single line), the depth of the recursion will be N, leading to O(N) space complexity
        return new_head