class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    count = 0
    res = None
    def dfs(node):
        nonlocal count
        nonlocal res
        if node is None: 
            return
        
        dfs(node.left)
        count += 1
        if count == k:
            res = node.val
            return
        dfs(node.right)

    dfs(root)
    return res


