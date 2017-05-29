package LinkedList._234_Palindrome_Linked_List;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-05-28.
 */
public class PalindromeLinkedListTest {
  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    ListNode n1 = new ListNode(2);
    ListNode n2 = new ListNode(3);
    ListNode n3 = new ListNode(4);
    ListNode n4 = new ListNode(3);
    ListNode n5 = new ListNode(2);
    ListNode n6 = new ListNode(1);

    head.next = n1;
    n1.next = n2;
    n2.next = n3;
    n3.next = n4;
    n4.next = n5;
    n5.next = n6;

    SingleLinkedList.printLinkedList(head);

    PalindromeLinkedList Test = new PalindromeLinkedList();
    System.out.println(Test.isPalindrome(head)); // Expected: true

    /*******************************************************/
    ListNode head_1 = new ListNode(1);
    ListNode n_1 = new ListNode(2);
    ListNode n_2 = new ListNode(3);
    ListNode n_3 = new ListNode(2);
    ListNode n_4 = new ListNode(4);

    head_1.next = n_1;
    n_1.next = n_2;
    n_2.next = n_3;
    n_3.next = n_4;

    SingleLinkedList.printLinkedList(head_1);

    PalindromeLinkedList Test2 = new PalindromeLinkedList();
    System.out.println(Test2.isPalindrome(head_1)); // Expected: false
  }
}
