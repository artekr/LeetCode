package LinkedList._237_Delete_Node_In_A_Linked_List;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-05-25.
 */
public class DeleteNodeInALinkedListTest {
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

    DeleteNodeInALinkedList Test = new DeleteNodeInALinkedList();
    Test.deleteNode(n3);

    // Expected: 1->2->3->5
    SingleLinkedList.printLinkedList(head);
  }
}
