from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        # Recursive cases
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
# Constructing the binary trees: p = [1, 2, 3], q = [1, 2, 3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

solution = Solution()
print(solution.isSameTree(p, q))  # Output: true

# Example 2: p = [1, 2], q = [1, null, 2]
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print(solution.isSameTree(p, q))  # Output: false

# Example 3: p = [1, 2, 1], q = [1, 1, 2]
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print(solution.isSameTree(p, q))  # Output: false

