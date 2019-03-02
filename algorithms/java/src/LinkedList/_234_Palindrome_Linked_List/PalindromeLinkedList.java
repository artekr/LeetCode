package LinkedList._234_Palindrome_Linked_List;

import DataStructure.ListNode;

import java.util.Stack;

/**
 * Created by hengwang on 2017-05-28.
 *
 * Given a singly linked list, determine if it is a palindrome.
 *
 * Follow up:
 * Could you do it in O(n) time and O(1) space?
 *
 */
public class PalindromeLinkedList {

  /**
   * 1. Copy the original linked list
   * 2. Reverse the original one
   * 3. Compare the two
   * @param head
   * @return
   */
  public boolean isPalindrome(ListNode head) {

    if (head == null) {
      return true;
    }

    // Copy the original Linked List
    ListNode copyHead = new ListNode(head.data);
    ListNode copyNext = copyHead;
    ListNode runner = head.next;
    copyHead.next = copyNext;
    while (runner != null) {
      ListNode n = new ListNode(runner.data);
      copyNext.next = n;
      copyNext = n;
      runner = runner.next;
    }

    // Reverse the original Linked list
    ListNode current = head;
    ListNode reversedHead = current;
    while (current != null) {
      ListNode next = current.next;
      current.next = reversedHead;
      reversedHead = current;
      current = next;
    }
    head.next = null;

    // Compare the reversed linked list with the copy linked list
    while (reversedHead != null) {
      if (reversedHead.data != copyHead.data) {
        return false;
      }
      reversedHead = reversedHead.next;
      copyHead = copyHead.next;
    }

    return true;
  }

  /**
   * Using runner approach and stack to store the half front nodes. And compare to the rest of the nodes.
   * @param head
   * @return
   */
  public boolean isPalindrome_IterateApproach(ListNode head) {
    if (head == null) {
      return true;
    }

    ListNode slow = head;
    ListNode fast = head;

    Stack<Integer> stack = new Stack<>();

    while (fast != null && fast.next != null) {
      stack.push(slow.data);
      slow = slow.next;
      fast = fast.next.next;
    }

    /* Has odd number of elements, so skip the middle element*/
    if (fast != null) {
      slow = slow.next;
    }

    while (slow != null) {
      if (slow.data != stack.pop()) {
        return false;
      }
      slow = slow.next;
    }

    return true;
  }

  /**
   *
   * @param head
   * @return
   */
  public boolean isPalindrome_LinearTime(ListNode head) {



    return true;
  }

}
