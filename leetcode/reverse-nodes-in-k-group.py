# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
            """Helper function to find the Kth node down the chain."""
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        # Anchor our list safely
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 1. Check if we have a full group of 'k' to reverse
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # 2. Reverse the group
            # We initialize prev to groupNext so the tail of our 
            # newly reversed group automatically connects to the next unreversed node!
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Re-wire the previous group to connect to our newly reversed group
            tmp = groupPrev.next # The original head of the group (now the tail)
            groupPrev.next = kth # Connect the previous chunk to the new head
            groupPrev = tmp      # Move our group start anchor forward
        
        # Complexity Analysis
        # Time Complexity O(N): Where N is the number of nodes in the list, We traverse each node at most twice (once to find the Kth node and once to reverse the group)
        # Space Complexity O(1): Since we are reversing the list in place and only using a few pointers for manipulation
        return dummy.next