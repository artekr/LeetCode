package LinkedList._142_Linked_List_Cycle_II;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-06-02.
 */
public class LinkedListCycleII {

  /**
   * (head to cycle start point)C = Cycle - S(slow moved in cycle)
   * @param head
   * @return
   */
  public ListNode detectCycle(ListNode head) {

    if (head == null) {
      return null;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (fast.next != null && fast.next.next != null) {
      slow = slow.next;
      fast = fast.next.next;
      // find cycle
      if (slow == fast) {
        ListNode copyHead = head;
        while (copyHead != slow) {
          slow = slow.next;
          copyHead = copyHead.next;
        }
        return slow;
      }
    }
    return null;
  }
}
