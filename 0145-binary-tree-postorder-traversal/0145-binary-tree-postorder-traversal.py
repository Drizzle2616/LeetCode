class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(currentNode, res):

            if not currentNode:
                return 
            
            dfs(currentNode.left, res)
            dfs(currentNode.right, res)
            res.append(currentNode.val)
            
        dfs(root, res)
        return res