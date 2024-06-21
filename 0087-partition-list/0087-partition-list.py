# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        firstHead = None
        firstTail = None
        secondHead = None
        secondTail = None

        if head == None:
            return head

        curr = head
        while curr != None:
            if curr.val < x:
                if firstHead == None:
                    firstHead = curr
                    firstTail = curr
                else:
                    firstTail.next = curr
                    firstTail = firstTail.next
            else:
                if secondHead == None:
                    secondHead = curr
                    secondTail = curr
                else:
                    secondTail.next = curr
                    secondTail = secondTail.next
            curr = curr.next

        if secondTail != None:
            secondTail.next = None
        if firstTail != None:
            firstTail.next = secondHead

        if firstHead != None:
            return firstHead
        return secondHead