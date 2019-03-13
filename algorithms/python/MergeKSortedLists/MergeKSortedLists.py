from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = point = ListNode(-1)

        while list1 and list2:
            if list1.val >= list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list2.next
            point = point.next

        if list1:
            point.next = list1
        else:
            point.next = list2
        return head.next

# list1: 1->2->4
list1 = ListNode(1)
list12 = ListNode(2)
list13 = ListNode(4)
list1.next = list12
list12.next = list13

# list1: 1->3->4
list2 = ListNode(1)
list22 = ListNode(3)
list23 = ListNode(4)
list2.next = list22
list22.next = list23

mergedList = Solution().mergeTwoLists(list1, list2)
while mergedList:
    print(mergedList.val)
    mergedList = mergedList.next