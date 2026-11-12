class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.current = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.current >= self.capacity:
            return False
        
        node = ListNode(value)
        prev = self.tail.prev 
        prev.next = node 
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.current += 1
        return True

    def deQueue(self) -> bool:
        if self.head.next == self.tail:
            return False

        temp = self.head.next
        self.head.next = temp.next
        self.current -= 1
        if temp.next == self.tail:
            self.tail.prev = self.head
            return True

        temp.next.prev = self.head
        return True

    def Front(self) -> int:
        return self.head.next.val if self.head.next.val != -1 else -1

    def Rear(self) -> int:
        return self.tail.prev.val if self.tail.prev.val != -1 else -1

    def isEmpty(self) -> bool:
        return True if self.current == 0 else False

    def isFull(self) -> bool:
        return True if self.current == self.capacity else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()