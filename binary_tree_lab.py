from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    # empty tree has depth 0
    if root is None:
        return 0
    
    # recursively find depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # return the larger depth + 1 for current node
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # if both nodes are smaller, go left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # if both nodes are larger, go right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # otherwise, current node is the split point (LCA)
    return root
