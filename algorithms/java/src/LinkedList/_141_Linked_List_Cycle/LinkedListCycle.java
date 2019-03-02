package LinkedList._141_Linked_List_Cycle;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-06-02.
 */
public class LinkedListCycle {

  /**
   * Two pointers - one slow (move one forward at a time), one fast (move two forward at a time).
   * @param head
   * @return
   */
  public boolean hasCycle(ListNode head) {

    if (head == null) {
      return false;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (slow != null && fast != null) {
      slow = slow.next;
      if (fast.next != null) {
        fast = fast.next.next;
      } else {
        return false;
      }
      if (slow == fast) {
        return true;
      }
    }
    return false;
  }

  /**
   * Simpler, from LeetCode
   * @param head
   * @return
   */
  public boolean hasCycle_Cleaner(ListNode head) {

    if (head == null) {
      return false;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (fast.next != null && fast.next.next != null) {
      // only check if fast reaches null
      slow = slow.next;
      fast = fast.next.next;
      if (slow == fast) {
        return true;
      }
    }
    return false;
  }

}
