package LinkedList._206_Reverse_Linked_List;

import DataStructure.ListNode;


/**
 * Created by hengwang on 2017-05-27.
 */
public class ReverseLinkedList {

  /**
   * Iterate the linked list, create a new head and assign it to the next one
   * @param head
   * @return
   */
  public ListNode reverseList_Iterate(ListNode head) {

    if (head == null) {
      return head;
    }

    ListNode current = head;
    ListNode newHead = current;

    while (current != null) {
      ListNode next = current.next;
      current.next = newHead;
      newHead = current;
      current = next;
    }
    // The old head becomes the tail of the new linked list, thus set the head.next = null.
    head.next = null;

    return newHead;
  }

  /**
   *
   * @param head
   * @return
   */
  public ListNode reverseList_Recurse(ListNode head) {

    return head;
  }
}
