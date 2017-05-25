package LinkedList._83_Remove_Duplicates_from_Sorted_List;

import DataStructure.ListNode;


/**
 * Created by hengwang on 2017-05-25.
 *
 * Given a sorted linked list, delete all duplicates such that each element appear only once.
 *
 * For example,
 * Given 1->1->2, return 1->2.
 * Given 1->1->2->3->3, return 1->2->3.
 *
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list/
 */
public class RemoveDuplicatesFromSortedList {

  public ListNode deleteDuplicates(ListNode head) {
    if (head == null) {
      return null;
    }

    ListNode current = head;
    ListNode faster = current.next;
    while (faster != null) {
      if (faster.data == current.data) {
        faster = faster.next;
        current.next = faster;
      } else {
        current = faster;
        faster = faster.next;
      }
    }
    return head;
  }

}
