package LinkedList._92_Reverse_Linked_List_II;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-05-27.
 */
public class ReverseLinkedListII {

  /**
   * Use a dummyHead to track the new head after each reverse
   * @param head
   * @param m
   * @param n
   * @return
   */
  public ListNode reverseBetween(ListNode head, int m, int n) {

    if (head == null) {
      return head;
    }

    ListNode current = head;
    ListNode innerTail = head;
    ListNode dummyHead = new ListNode(0);
    dummyHead.next = head;
    // Used to locate the new head of the list
    head = dummyHead;

    int i = 0;
    while ( i < n) {
      ListNode next = current.next;
      if (i < m - 1) {
        innerTail = next;
        dummyHead = dummyHead.next;
      } else {
        current.next = dummyHead.next;
        dummyHead.next = current;
      }
      i++;
      current = next;
    }
    innerTail.next = current;

    return  head.next;
  }
}
