from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Choose the middle element of the current subarray
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            
            return node
        
        return convert(0, len(nums) - 1)

# Example usage:
solution = Solution()

# Example 1
nums1 = [-10, -3, 0, 5, 9]
tree1 = solution.sortedArrayToBST(nums1)

# Function to print the tree in level order to verify the structure
from collections import deque

def print_tree(root: Optional[TreeNode]):
    if not root:
        return "[]"
    result = []
    queue = deque([root])
    while queue:
        nod
