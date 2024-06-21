# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do bfs with switching between popleft and pop
        if not root:
            return 
        ans = []
        queue = deque([root])
        flip = 1
        while queue:
            n = len(queue)
            levelVal = []
            for _ in range(n):
                node = queue.popleft()
                levelVal.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(levelVal[::flip])
            flip *= -1
        return ans    