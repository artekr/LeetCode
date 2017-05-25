package LinkedList._83_Remove_Duplicates_from_Sorted_List;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-05-25.
 */
public class RemoveDuplicatesFromSortedListTest {
  public static void main(String[] args) {

    ListNode head = new ListNode(2);
    ListNode n1 = new ListNode(3);
    ListNode n2 = new ListNode(5);
    ListNode n3 = new ListNode(5);
    ListNode n4 = new ListNode(6);
    ListNode n5 = new ListNode(7);
    ListNode n6 = new ListNode(7);

    head.next = n1;
    n1.next = n2;
    n2.next = n3;
    n3.next = n4;
    n4.next = n5;
    n5.next = n6;

    SingleLinkedList.printLinkedList(head);

    RemoveDuplicatesFromSortedList Test = new RemoveDuplicatesFromSortedList();

    ListNode newHead = Test.deleteDuplicates(head);

    SingleLinkedList.printLinkedList(newHead);

  }
}
