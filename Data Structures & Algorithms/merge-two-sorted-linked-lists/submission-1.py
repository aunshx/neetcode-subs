# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sol = ListNode(0)
        d3 = sol

        while list1 and list2:
            if list1.val > list2.val:
                d3.next = list2
                list2 = list2.next
            else:
                d3.next = list1
                list1 = list1.next
        
            d3 = d3.next

        d3.next = list1 if list1 else list2

        return sol.next