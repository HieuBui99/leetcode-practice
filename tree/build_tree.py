from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
        # recursively build the left and right subtree
        # the root is the first element in preorder
        if not preorder or not inorder:
            return None
        
        node_index = {}
        for i, val in enumerate(inorder):
            node_index[val] = i
        root = TreeNode(preorder[0])
        mid = node_index[root.val]

        root.left = build_tree(preorder[1:mid+1], inorder[:mid])
        root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
        return root