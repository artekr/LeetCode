
## 142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

**Note:** Do not modify the linked list.

**Follow up:** <br>
Can you solve it without using extra space?

*[Link](https://leetcode.com/problems/linked-list-cycle-ii)*


---
> **Hint:** <br>
Definitions:
Cycle = length of the cycle, if exists.
C is the beginning of Cycle, S is the distance of slow pointer from C when slow pointer meets fast pointer.

> Distance(slow) = C + S, Distance(fast) = 2 * Distance(slow) = 2 * (C + S). To let slow pointer meets fast pointer, 
only if fast pointer run 1 cycle more than slow pointer. <br> 
Distance(fast) - Distance(slow) = Cycle <br>
=> 2 * (C + S) - (C + S) = Cycle <br>
=> C + S = Cycle <br>
=> C = Cycle - S <br>
=> This means if slow pointer runs (Cycle - S) more, it will reaches C. So at this time, if there's another point2 running from head <br>
=> After C distance, point2 will meet slow pointer at C, where is the beginning of the cycle. <br>