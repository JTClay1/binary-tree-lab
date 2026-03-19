from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    # Base case: an empty tree has depth 0
    if root is None:
        return 0

    # Recursively find the depth of the left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Return the larger depth, plus 1 for the current node
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # If both nodes are smaller than root, LCA must be in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # If both nodes are greater than root, LCA must be in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Otherwise, this root is the split point and therefore the LCA
    return root