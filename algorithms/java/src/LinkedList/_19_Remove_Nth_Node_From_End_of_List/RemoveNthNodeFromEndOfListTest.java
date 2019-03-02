package LinkedList._19_Remove_Nth_Node_From_End_of_List;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-05-25.
 */
public class RemoveNthNodeFromEndOfListTest {

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

    RemoveNthNodeFromEndOfList Test = new RemoveNthNodeFromEndOfList();
//    ListNode newHead = Test.removeNthFromEnd(head, 5);
    ListNode newHead = Test.removeNthFromEnd_OnePass(head, 3);

    SingleLinkedList.printLinkedList(newHead);
  }
}
