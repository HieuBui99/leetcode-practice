class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    first =  head
    # dummy node cause 1 element edge case
    dummy = ListNode(None, head)
    second = dummy
    while n > 0:
        n -= 1
        first = first.next

    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next