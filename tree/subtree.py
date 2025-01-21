from same import is_same_tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(root: TreeNode, sub_root: TreeNode) -> bool:
    if not sub_root:
        return True
    if not root:
        return False

    res = is_same_tree(root, sub_root)
    if res:
        return True
    
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
