# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        if N == 0:
            return []
        
        if N == 1:
            return lists[0]

        temp = ListNode()
        curr = temp
        i = 1
        
        while i < N:
            list1 = lists[i - 1]
            list2 = lists[i]

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next

                curr = curr.next
            
            curr.next = list1 or list2
            i += 1

        # Complexity Analysis
        # Time Complexity O(N * M): Where N is the number of linked lists and M is the average number of nodes in each 
        #                           linked list. We are merging N linked lists, and each merge operation takes O(M) time
        # Space Complexity O(1): Since we are using only a constant amount of extra space to store the merged linked 
        #                        list. We are not using any additional data structures that grow with the input size
        return temp.next


    def mergeKListsOptimized(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            """Standard helper function to merge two lists in O(1) space."""
            dummy = ListNode(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
                
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
            
        while len(lists) > 1:
            merged_lists = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                merged_lists.append(self.mergeTwoLists(list1, list2))
                
            lists = merged_lists
        
        # Complexity Analysis
        # Time Complexity O(N log K): Where N is the total number of nodes across all linked lists and K is the number 
        #                             of linked lists. The merge operation is performed log K times (due to the divide 
        #                             and conquer approach), and each merge operation takes O(N) time in the worst case 
        #                             when all nodes are merged together
        # Space Complexity O(1): Since we are using only a constant amount of extra space to store the merged linked 
        #                        list. We are not using any additional data structures that grow with the input size
        return lists[0]