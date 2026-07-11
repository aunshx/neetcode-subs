# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            curr = lists[i]

            while curr:
                heap.append(curr.val)
                curr = curr.next

        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while len(heap):
            node = ListNode(heapq.heappop(heap))
            curr.next = node
            curr = curr.next

        
        return dummy.next