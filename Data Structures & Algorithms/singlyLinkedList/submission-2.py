class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if self.size <= index:
            return -1
        curr = self.head.next
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.val
        

    def insertHead(self, val: int) -> None:
        curr = self.head 
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if self.tail == self.head: 
            self.tail = node
        self.size += 1

        
    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if self.size <= index:
            return False
        curr = self.head 
        while index > 0:
            curr = curr.next
            index -= 1
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        self.size -= 1  
        return True
        

    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr.next:
            curr = curr.next
            res.append(curr.val)
        return res
