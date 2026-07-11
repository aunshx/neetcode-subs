# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head 

        while dummy and dummy.next:
            node = ListNode()
            node.val = math.gcd(dummy.val, dummy.next.val)
            temp = dummy.next 
            dummy.next = node
            node.next = temp 
            dummy = node.next

        return head