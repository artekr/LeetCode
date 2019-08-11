# Definition for a list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Implementation for Stack as a linked list
class LinkedListAsStack:

    first = None

    def push(self, item: ListNode):
        if self.first is not None:
            item.next = self.first        
        self.first = item

    def pop(self) -> ListNode:
        if self.first is None:
            return None
        item = self.first
        self.first = self.first.next
        return item

    def isEmpty(self):
        return self.first is None


stack = LinkedListAsStack()
stack.push(ListNode(1))
stack.push(ListNode(2))
stack.push(ListNode(3))

x = stack.pop()

print("x is: ", x.val)

