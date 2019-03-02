package LinkedList._21_Merge_Two_Sorted_Lists;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-06-03.
 */
public class MergeTwoSortedListsTest {

  public static void main(String[] args) {

    ListNode headA = new ListNode(1);
    ListNode nA2 = new ListNode(3);
    ListNode nA3 = new ListNode(6);
    ListNode nA4 = new ListNode(7);

    headA.next = nA2;
    nA2.next = nA3;
    nA3.next = nA4;

    SingleLinkedList.printLinkedList(headA);

    ListNode headB = new ListNode(2);
    ListNode nB2 = new ListNode(4);
    ListNode nB3 = new ListNode(5);

    headB.next = nB2;
    nB2.next = nB3;

    SingleLinkedList.printLinkedList(headB);

    MergeTwoSortedLists Test = new MergeTwoSortedLists();
    ListNode newHead = Test.mergeTwoLists(headA, headB);

    SingleLinkedList.printLinkedList(newHead);
  }
}
