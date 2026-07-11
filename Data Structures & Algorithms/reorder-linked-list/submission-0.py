class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        slow = slow.next
        mid.next = None 

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        head1 = head
        second = prev
        while second:
            temp1 = head1.next
            temp2 = second.next
            head1.next = second
            second.next = temp1
            head1 = temp1
            second = temp2