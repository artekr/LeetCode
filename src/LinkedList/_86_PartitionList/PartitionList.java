package LinkedList._86_PartitionList;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-05-26.
 */
public class PartitionList {

  /**
   * Create two new linked list to store the left and right, then merge them into one.
   *
   * This approach is mostly "stable" in that elements stay in their original order, other than the necessary
   * movement around the partition.
   *
   * @param head
   * @param x
   * @return
   */
  public ListNode partition(ListNode head, int x) {

    ListNode current = head;
    ListNode leftStart = null, left = null, rightStart = null, right = null;

    while (current != null) {
      ListNode next = current.next;
      current.next = null;
      if (current.data < x) {
        if (left == null) {
          leftStart = current;
          left = leftStart;
        } else {
          left.next = current;
          left = left.next;
        }
      } else {
        if (right == null) {
          rightStart = current;
          right = rightStart;
        } else {
          right.next = current;
          right = right.next;
        }
      }
      current = next;
    }
    if (leftStart == null) {
      return rightStart;
    }

    left.next = rightStart;

    return leftStart;
  }

}
