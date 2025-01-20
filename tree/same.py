class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    stack_p = [p]
    stack_q = [q]
    while stack_p and stack_q:
        if stack_p:
            node_p = stack_p.pop()
        if stack_q:
            node_q = stack_q.pop()
        
        if node_p or node_q:
            if node_p is None or node_q is None or node_p.val != node_q.val:
                return False
            if node_p:
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
            if node_q:
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
            
    return True 