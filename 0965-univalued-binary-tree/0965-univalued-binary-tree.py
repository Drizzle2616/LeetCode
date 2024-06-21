class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def unique(root,x):
            if not root:
                return True
            if root.val!=x:
                return False
            return unique(root.left,x) and unique(root.right,x)
        return unique(root,root.val)