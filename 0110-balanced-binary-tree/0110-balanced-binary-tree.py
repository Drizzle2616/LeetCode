from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0
            
            left_balanced, left_height = check_balance_and_height(node.left)
            right_balanced, right_height = check_balance_and_height(node.right)
            
            current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            current_height = max(left_height, right_height) + 1
            
            return current_balanced, current_height
        
        balanced, _ = check_balance_and_height(root)
        return balanced
