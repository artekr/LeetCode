package LinkedList._142_Linked_List_Cycle_II;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-06-02.
 */
public class LinkedListCycleIITest {

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
    n5.next = n2;

    LinkedListCycleII Test = new LinkedListCycleII();
    System.out.println(Test.detectCycle(head).data); // Expected: true

    /**************************************************************/
    ListNode head_2 = new ListNode(1);
    ListNode n2_2 = new ListNode(2);
    ListNode n3_2 = new ListNode(3);
    ListNode n4_2 = new ListNode(4);

    head_2.next = n2_2;
    n2_2.next = n3_2;
    n3_2.next = n4_2;

    System.out.println(Test.detectCycle(head_2)); // Expected: null


  }
}
