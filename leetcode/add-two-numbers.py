# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        curr3 = ListNode(None)
        last_digit = 0
        remaining = 0

        while curr1 and curr2:
            summ = curr1.val + curr2.val + remaining
            
            # Check if summ is more than one digit
            last_digit = summ % 10
            remaining = summ // 10

            curr3.val = last_digit
            curr3.next = ListNode(None)
            curr3 = curr3.next

            curr1 = curr1.next
            curr2 = curr2.next

        # Check remaining curr1
        while curr1:
            break

        # Check remaining curr2
        while curr2:
            break

        # Complexity Analysis
        # Time Complexity O(max(M, N)): Let M and N be the number of nodes in the linked lists l1 and l2, respectively. The while loop 
        #                               iterates through both linked lists simultaneously, and the number of iterations is determined by
        #                               the longer linked list. Therefore, the time complexity is O(max(M, N))
        # Space Complexity O(max(M, N)): We are creating a new linked list to store the result, and in the worst case, the length of the 
        #                                resulting linked list can be at most max(M, N) + 1 (if there is a carry from the last 
        #                                addition). Therefore, the space complexity is O(max(M, N))
        return curr3


    def addTwoNumbersOptimized(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Use a dummy node to anchor the head of the new list
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Step 2: Loop as long as there is data in l1, l2, OR a carry to process
        while l1 or l2 or carry:
            # Get values (use 0 if a list is already exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Step 3: Attach the new node
            curr.next = ListNode(total % 10)
            
            # Move pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Complexity Analysis
        # Time Complexity O(max(M, N)): Let M and N be the number of nodes in the linked lists l1 and l2, respectively. The while loop iterates 
        #                               through both linked lists simultaneously, and the number of iterations is determined by the longer linked 
        #                               list. Therefore, the time complexity is O(max(M, N))
        # Space Complexity O(max(M, N)): We are creating a new linked list to store the result, and in the worst case, the length of the resulting 
        #                                linked list can be at most max(M, N) + 1 (if there is a carry from the last addition). Therefore, the space 
        #                                complexity is O(max(M, N))
        return dummy.next