# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        curr = slow.next
        mid.next = None
        prev = None
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp
        res = 0
        left, right = head, prev
        while right:
            res = max(res, left.val + right.val)
            left = left.next
            right = right.next
        return res
