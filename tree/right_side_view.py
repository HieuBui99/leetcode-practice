from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> List[int]:
    if root is None: 
        return []
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        len_q = len(queue)
        for i in range(len_q):
            node = queue.popleft()
            if node:
                if i == len_q - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    return res