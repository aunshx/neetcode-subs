# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        d = head
        while d:
            d = d.next
            k += 1

        if n == k:
            return head.next

        d = head
        count = 1

        while d and d.next:
            if count == (k-n):
                d.next = d.next.next
            count += 1
            d = d.next

        return head
        