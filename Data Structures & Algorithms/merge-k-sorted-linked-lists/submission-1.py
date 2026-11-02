# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        heap = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heappush(heap, head.val)
                head = head.next

        res = ListNode(0)
        dummy = res
        while heap:
            val = heappop(heap)
            dummy.next = ListNode(val)
            dummy = dummy.next

        return res.next



        