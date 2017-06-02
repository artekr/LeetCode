package LinkedList._160_Intersection_Of_Two_Linked_Lists;

import DataStructure.ListNode;
import static java.lang.Math.abs;

/**
 * Created by hengwang on 2017-06-02.
 */
public class IntersectionOfTwoLinkedLists {

  /**
   * What's the characteristic of the two list after the node right before the intersection ?
   * What about the length ?
   * @param headA
   * @param headB
   * @return
   */
  public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

    if (headA == null || headB == null) {
      return null;
    }

    // Get the lengths of two lists
    ListNode currentA = headA;
    ListNode currentB = headB;
    int lengthA = 0;
    int lengthB = 0;
    while (currentA != null) {
      lengthA++;
      currentA = currentA.next;
    }
    while (currentB != null) {
      lengthB++;
      currentB = currentB.next;
    }

    // Move the longer list to align with the shorter one
    int gap = lengthA - lengthB;
    ListNode runnerA = headA;
    ListNode runnerB = headB;
    if (gap >= 0) {
      for (int i = 0; i < gap; i++) {
        runnerA = runnerA.next;
      }
    } else {
      for (int i = 0; i < abs(gap); i++) {
        runnerB = runnerB.next;
      }
    }

    // Now two lists have same length, move one at a time and compare
    while (runnerA != null) {
      if (runnerA == runnerB) {
        return runnerA;
      }
      runnerA = runnerA.next;
      runnerB = runnerB.next;
    }

    return null;
  }

  /**
   * From LeetCode solution!
   * Actually we don't care about the "value" of difference, we just want to make sure two pointers reach the
   * intersection node at the same time.
   * We can use two iterations to do that. In the first iteration, we will reset the pointer of one linkedlist to the
   * head of another linkedlist after it reaches the tail node. In the second iteration, we will move two pointers
   * until they points to the same node. Our operations in first iteration will help us counteract the difference.
   * So if two linkedlist intersects, the meeting point in second iteration must be the intersection point. If the
   * two linked lists have no intersection at all, then the meeting pointer in second iteration must be the tail node
   * of both lists, which is null.
   *
   * @param headA
   * @param headB
   * @return
   */
  public ListNode getIntersectionNode_NoLengthDifference(ListNode headA, ListNode headB) {
    //boundary check
    if (headA == null || headB == null) return null;

    ListNode a = headA;
    ListNode b = headB;

    //if a & b have different len, then we will stop the loop after second iteration
    while (a != b) {
      //for the end of first iteration, we just reset the pointer to the head of another linkedlist
      a = a == null ? headB : a.next;
      b = b == null ? headA : b.next;
    }

    return a;
  }

}
