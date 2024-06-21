"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Use bfs
        que = deque()
        que.append(root)
        while que and que[0]:
            length = len(que)
            for i in range(length):
                curr = que.popleft()
                curr.next = que[0] if i+1 < length else None
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                
        return root