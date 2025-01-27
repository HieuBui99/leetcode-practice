class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    if root is None:
        return False

    stack = []
    stack.append((root, -float("inf"), float("inf")))

    while stack:
        node, left, right = stack.pop()

        if not (left < node.val < right):
            return False
        if node.left:
            stack.append((node.left, left, node.val))
        if node.right:
            stack.append((node.right, node.val, right))

    return True
