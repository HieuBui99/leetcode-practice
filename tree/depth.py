class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

    # stack = []
    # stack.append((root, 1))
    # res = 0
    # while stack:
    #     node, depth = stack.pop()

    #     if node:
    #         res = max(res, depth)
    #         stack.append((node.left, depth+1))
    #         stack.append((node.right, depth+1))
    # return res