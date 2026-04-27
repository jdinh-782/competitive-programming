# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        curr = head

        while curr:
            temp = curr.next
            curr = curr.next

        curr = head
        while temp:
            while curr:
                if temp.random == curr:
                    temp.next = curr

                curr = curr.next

            temp = temp.next

        # Complexity Analysis
        # Time Complexity O(N^2): Let N be the number of nodes in the linked list. The first while loop traverses the list once, resulting 
        #                         in O(N) time complexity. The second while loop is nested inside the first loop and also traverses the list 
        #                         once for each node, resulting in O(N) time complexity for each iteration of the outer loop. Therefore, 
        #                         the overall time complexity is O(N * N) = O(N^2)
        # Space Complexity O(N): We are creating new nodes for each node in the original list, which requires O(N) space. Additionally, we 
        #                        are using a few pointers (temp and curr) that take O(1) space, but the dominant factor is the space used 
        #                        for the new nodes, resulting in O(N) space complexity
        return temp


    def copyRandomListOptimized(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # STEP 1: Clone and Weave
        # A -> B -> C  becomes  A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            clone = Node(curr.val, curr.next)
            curr.next = clone
            curr = clone.next
            
        # STEP 2: Assign Random Pointers
        curr = head
        while curr:
            if curr.random:
                # The clone is curr.next. 
                # The clone's random target is the clone of curr's random target!
                curr.next.random = curr.random.next
            curr = curr.next.next # Skip to the next original node
            
        # STEP 3: Unweave the lists
        curr = head
        copy_head = head.next
        
        while curr:
            clone = curr.next
            
            # Restore original list pointer
            curr.next = clone.next
            # Step original pointer forward
            curr = curr.next 
            
            # Wire up the cloned list pointer
            if curr:
                clone.next = curr.next
        
        # Complexity Analysis
        # Time Complexity O(N): Let N be the number of nodes in the linked list. Each of the three steps (cloning and weaving, assigning random pointers, and unweaving) 
        #                       traverses the list at most once, resulting in O(N) time complexity
        # Space Complexity O(1): We are using only constant space to store the pointers curr and clone. The cloned nodes are interleaved with the original nodes, so 
        #                        we are not using any additional space for new nodes, resulting in O(1) space complexity
        return copy_head