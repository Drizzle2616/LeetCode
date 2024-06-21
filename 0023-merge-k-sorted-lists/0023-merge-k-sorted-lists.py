# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        if not values:
            return None

        heapq.heapify(values)
        dummy = ListNode(0)
        curr = dummy
        
        while values:
            val = heapq.heappop(values)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next



