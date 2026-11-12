"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        m = {}
        curr = head
        while curr:
            m[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                m[curr].next = m[curr.next]
            if curr.random:
                m[curr].random = m[curr.random]
            curr = curr.next

        return m[head]
        