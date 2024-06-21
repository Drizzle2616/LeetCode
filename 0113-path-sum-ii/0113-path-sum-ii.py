# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(root,path,rem_sum):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and rem_sum==root.val:
                ans.append(path.copy())
            backtrack(root.left,path,rem_sum-root.val)
            backtrack(root.right,path,rem_sum-root.val)
            path.pop()
        ans=[]
        if root is None:
            return []
        backtrack(root,[],targetSum)
        return ans
        