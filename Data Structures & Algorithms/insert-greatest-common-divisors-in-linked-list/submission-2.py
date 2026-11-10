# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a,b):
        while b:
            a,b=b,a%b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = head 

        while d and d.next:
            val = ListNode(self.gcd(d.val,d.next.val))
            temp = d.next
            d.next = val
            val.next = temp
            d = d.next.next

        return head 
        