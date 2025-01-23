from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    nodes = []
    queue = deque()
    queue.append(root)
    while queue:
        level = []
        q_len = len(queue)
        for i in range(q_len):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            nodes.append(level)
    return nodes