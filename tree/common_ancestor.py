class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    curr = root
    while curr:
        if curr.val > p.val and curr.val > q.val:
            curr = curr.left
        elif curr.val < p.val and curr.val < q.val:
            curr = curr.right
        else:
            return curr
    