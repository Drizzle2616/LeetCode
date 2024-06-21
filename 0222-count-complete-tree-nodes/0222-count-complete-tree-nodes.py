# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.right is None:
            return 2
        left_level = self.level(root.left)
        right_level = self.level(root.right)
        if left_level == right_level:
            return 2 ** left_level + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2 ** right_level

    def level(self, root):
        i = 0
        while root:
            i += 1
            root = root.left
        return i
