package LinkedList._86_PartitionList;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-05-26.
 */
public class PartitionListTest {

  public static void main(String[] args) {
    ListNode head = new ListNode(3);
    ListNode n1 = new ListNode(5);
    ListNode n2 = new ListNode(8);
    ListNode n3 = new ListNode(5);
    ListNode n4 = new ListNode(10);
    ListNode n5 = new ListNode(2);
    ListNode n6 = new ListNode(1);

    head.next = n1;
    n1.next = n2;
    n2.next = n3;
    n3.next = n4;
    n4.next = n5;
    n5.next = n6;

    SingleLinkedList.printLinkedList(head);

    PartitionList Test = new PartitionList();

    ListNode newHead1 = Test.partition(head, 5);
    SingleLinkedList.printLinkedList(newHead1); // Expected: 3->2->1->5->8->5->10

    // Test Case 2
    ListNode head_1 = new ListNode(1);

    SingleLinkedList.printLinkedList(head_1);

    ListNode new_head_1 = Test.partition(head_1, 0);
    SingleLinkedList.printLinkedList(new_head_1); // Expected: 1
  }

}
