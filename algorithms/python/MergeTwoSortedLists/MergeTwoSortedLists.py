# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        head = ListNode(-1)
        result = head
        while l1 and l2:
            if l1.val > l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next
            result = result.next
        if l1:
            result.next = l1
        if l2:
            result.next = l2
        return head.next