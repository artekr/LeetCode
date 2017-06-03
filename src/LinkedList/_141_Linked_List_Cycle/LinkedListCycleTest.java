package LinkedList._141_Linked_List_Cycle;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-06-02.
 */
public class LinkedListCycleTest {

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    ListNode n2 = new ListNode(2);
    ListNode n3 = new ListNode(3);
    ListNode n4 = new ListNode(4);
    ListNode n5 = new ListNode(5);

    head.next = n2;
    n2.next = n3;
    n3.next = n4;
    n4.next = n5;
    n5.next = head;

    LinkedListCycle Test = new LinkedListCycle();
    System.out.println(Test.hasCycle(head)); // Expected: true
    System.out.println(Test.hasCycle_Cleaner(head)); // Expected: true

    /**************************************************************/
    ListNode head_2 = new ListNode(1);
    ListNode n2_2 = new ListNode(2);
    ListNode n3_2 = new ListNode(3);
    ListNode n4_2 = new ListNode(4);

    head_2.next = n2_2;
    n2_2.next = n3_2;
    n3_2.next = n4_2;

    System.out.println(Test.hasCycle(head_2)); // Expected: false
    System.out.println(Test.hasCycle_Cleaner(head_2)); // Expected: false

  }
}
