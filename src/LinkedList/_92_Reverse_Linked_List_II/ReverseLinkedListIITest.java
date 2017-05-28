package LinkedList._92_Reverse_Linked_List_II;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;
import LinkedList._206_Reverse_Linked_List.ReverseLinkedList;

/**
 * Created by hengwang on 2017-05-27.
 */
public class ReverseLinkedListIITest {

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

    ReverseLinkedListII Test = new ReverseLinkedListII();
    ListNode newHead = Test.reverseBetween(head, 3, 4);

    SingleLinkedList.printLinkedList(newHead); // Expected: 1->4->3->2->5

    /***********************************************************************/
    ListNode head_1 = new ListNode(1);
    ListNode n_1 = new ListNode(2);
    ListNode n_2 = new ListNode(3);

    head_1.next = n_1;
    n_1.next = n_2;

    SingleLinkedList.printLinkedList(head_1);

    ListNode newHead_1 = Test.reverseBetween(head_1, 1, 2);

    SingleLinkedList.printLinkedList(newHead_1); // Expected: 2->1
  }
}
