# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        curr.next = list1 or list2

        # Complexity Analysis
        # Time Complexity O(N + M): Let N and M be the number of nodes in list1 and list2 respectively. The while loop iterates 
        #                           through both lists once, resulting in O(N + M) time complexity
        # Space Complexity O(1): We are using only constant space to store the pointers temp and curr. The merged list is built 
        #                        by reusing the existing nodes from list1 and list2, so we are not using any additional space for new nodes
        return temp.next

    
    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base Cases: If one list is empty, return the other
        if not list1:
            return list2
        if not list2:
            return list1
            
        # Recursive Step: Determine the smaller node, then set its 'next' 
        # to the result of merging the remainder of the lists.
        if list1.val < list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)

            # Complexity Analysis
            # Time Complexity O(N + M): Let N and M be the number of nodes in list1 and list2 respectively. The recursive function is 
            #                           called once for each node in both lists, resulting in O(N + M) time complexity
            # Space Complexity O(N + M): The space complexity is O(N + M) because of the recursive call stack. In the worst case, 
            #                            when all nodes of one list are smaller than the other, the depth of the recursion will be N + M, 
            #                            leading to O(N + M) space complexity
            return list2