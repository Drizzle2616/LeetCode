from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point
            current = stack.pop()
            result.append(current.val)  # Add the node value to result
            current = current.right  # Visit the right subtree
        
        return result

# Example usage:
# Constructing the binary tree: [1, null, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2]

# Example 2: Empty tree
root = None
print(solution.inorderTraversal(root))  # Output: []

# Example 3: Single node tree
root = TreeNode(1)
print(solution.inorderTraversal(root))  # Output: [1]
