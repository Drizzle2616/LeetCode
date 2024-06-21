from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # If we reach a leaf node, check if the targetSum is met
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Subtract the current node's value from the target sum
        targetSum -= root.val
        
        # Recursively check the left and right subtree
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Example usage:
# Building the binary tree for the given example
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

solution = Solution()
print(solution.hasPathSum(root, 22))  # Output: true
