package LinkedList._19_Remove_Nth_Node_From_End_of_List;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-05-25.
 *
 * LeetCode:
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list
 */
public class RemoveNthNodeFromEndOfList {

  /**
   * Naive approach
   * Count the number of elements in linked list first,
   * Calculate the index from the head based on n and count.
   * Find the ListNode right before the Nth node from end.
   * Delete the Nth node
   * @param head
   * @param n
   * @return
   */
  public ListNode removeNthFromEnd(ListNode head, int n) {
    int count = 0;
    ListNode current = head;
    while (current != null) {
      current = current.next;
      count++;
    }

    // Special case when Nth from end is the head of linked list
    if (n == count) {
      head = head.next;
      return head;
    }

    int index = 1;
    ListNode runner = head;
    while (index < count - n) {
      runner = runner.next;
      index++;
    }
    runner.next = runner.next.next;

    return head;
  }

  /**
   * Inspired From LeetCode:
   * A one pass solution can be done using pointers. Move one pointer fast --> n places forward, to maintain a
   * gap of n-1 between the two pointers and then move both at the same speed.
   *
   * @param head
   * @param n
   * @return
   */
  public ListNode removeNthFromEnd_OnePass(ListNode head, int n) {

    ListNode slow = head;
    ListNode fast = head;
    // Build the gap between fast and slow
    for (int i = 0; i < n; i++) {
      fast = fast.next;
      // When n happens to be the first element in linked list
      if (fast == null) {
        head = head.next;
        return head;
      }
    }
    while (fast.next != null) {
      fast = fast.next;
      slow = slow.next;
    }
    slow.next = slow.next.next;
    return head;
  }

}
