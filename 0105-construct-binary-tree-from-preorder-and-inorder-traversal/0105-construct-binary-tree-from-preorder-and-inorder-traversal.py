# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(preorder[0])
        stack = [root]
        iIdx = 0
        for pIdx in range(1, len(preorder)):
            currentVal = preorder[pIdx]
            currentNode = stack[-1]

            # Add to left
            if currentNode.val != inorder[iIdx]:

                currentNode.left = TreeNode(currentVal)
                stack.append(currentNode.left)

            # Add to right
            else:
                while stack and stack[-1].val == inorder[iIdx]:
                    currentNode = stack.pop()
                    iIdx += 1
                          
                currentNode.right = TreeNode(currentVal)
                stack.append(currentNode.right) 
            
        return root