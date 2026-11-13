# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d = ListNode(-1)
        d.next = head
        curr = d
        dummy = head
        n = 0

        while dummy:
            dummy = dummy.next
            n += 1

        i=0
        group_prev = d
        curr = head
        while i+k<=n:
            group_head = curr
            prev = None
            j = i + k
            while i < j:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            group_prev.next = prev
            group_head.next = curr
            group_prev = group_head

        return d.next