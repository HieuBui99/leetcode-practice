class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode) -> None:
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #slow at mid
    second = slow.next 
    #reverse
    slow.next = None
    prev = None
    while second:
        # o -> o -> o
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    second = prev 
    first = head
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2