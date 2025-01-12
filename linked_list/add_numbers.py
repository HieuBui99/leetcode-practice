class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    curr_l1 = l1
    curr_l2 = l2
    sum_head = ListNode()
    carry = 0
    curr = sum_head
    while curr_l1 or curr_l2:
        v1 = curr_l1.val if curr_l1 else 0
        v2 = curr_l2.val if curr_l2 else 0
        val = v1 + v2 + carry
        if val >= 10:
            carry = val // 10
            val = val - 10
        else:
            carry = 0
        new_node = ListNode(val=val)
        curr.next = new_node
        curr = new_node
        
        curr_l1 = curr_l1.next if curr_l1 else None
        curr_l2 = curr_l2.next if curr_l2 else None

    if carry:
        new_node = ListNode(val=carry)
        curr.next = new_node
    return sum_head.next