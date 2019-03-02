
## 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in **constant** time.

* _push(x)_  -- Push element x onto stack.
* _pop()_    -- Removes the element on top of the stack.
* _top()_    -- Get the top element.
* _getMin()_ -- Retrieve the minimum element in the stack.

**Example:**

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

*[Link](https://leetcode.com/problems/min-stack)*