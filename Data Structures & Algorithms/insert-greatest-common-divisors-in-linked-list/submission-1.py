# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head 
        def gcd(a,b):
            while b > 0:
                temp = a
                a = b
                b = temp%b
            return a

        while dummy and dummy.next:
            node = ListNode()
            node.val = gcd(dummy.val, dummy.next.val)
            temp = dummy.next 
            dummy.next = node
            node.next = temp 
            dummy = node.next

        return head