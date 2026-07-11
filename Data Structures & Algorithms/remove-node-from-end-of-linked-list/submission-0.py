# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nlen = 0

        d = head
        while d:
            nlen += 1
            d = d.next

        if nlen == n:
            return head.next
            
        d = head
        count = 1
        while d:
            if nlen-count == n:
                d.next = d.next.next
                break
            count += 1
            d = d.next
        
        return head
        