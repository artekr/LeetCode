package LinkedList._206_Reverse_Linked_List;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-05-27.
 */
public class ReverseLinkedListTest {

  public static void main(String[] args) {

    ListNode head = new ListNode(1);
    ListNode n1 = new ListNode(2);
    ListNode n2 = new ListNode(3);
    ListNode n3 = new ListNode(4);
    ListNode n4 = new ListNode(5);

    head.next = n1;
    n1.next = n2;
    n2.next = n3;
    n3.next = n4;

    SingleLinkedList.printLinkedList(head);

    ReverseLinkedList Test = new ReverseLinkedList();
    ListNode newHead = Test.reverseList_Iterate(head);

    SingleLinkedList.printLinkedList(newHead); // Expected: 5->4->3->2->1
    SingleLinkedList.printLinkedList(head);
  }
}
