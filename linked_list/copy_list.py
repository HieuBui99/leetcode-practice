class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    if not head:
        return None

    nodes = {None: None}
    curr = head
    while curr:
        new_node = Node(curr.val)
        nodes[curr] = new_node
        curr = curr.next
    curr = head
    while curr:
        copy = nodes[curr]
        copy.next = nodes[curr.next]
        copy.random = nodes[curr.random] if curr.random else None
        curr = curr.next
    return nodes[head]
