class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root: TreeNode) -> int:
    # track maximum value along a path
    if root is None:
        return 0
    
    res = 0
    stack = []
    stack.append((root, -float("inf")))
    while stack:
        node, max_val = stack.pop()
        if node.val >= max_val:
            res += 1
        
        if node.left:
            stack.append((node.left, max(node.val, max_val)))
        if node.right:
            stack.append((node.right, max(node.val, max_val)))

    return res