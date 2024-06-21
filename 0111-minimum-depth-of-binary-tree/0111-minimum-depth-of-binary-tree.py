from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # The queue holds tuples of (node, current_depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if the node is a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add the children to the queue with an incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

# Example usage:
# Building the binary tree for the given example
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.minDepth(root))  # Output: 2
