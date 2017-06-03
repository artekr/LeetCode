package LinkedList._21_Merge_Two_Sorted_Lists;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-06-03.
 */
public class MergeTwoSortedLists {

  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

    if (l1 == null) return l2;
    if (l2 == null) return l1;

    ListNode dummy = new ListNode(0);
    ListNode result = dummy;

    while (l1 != null && l2 != null) {
      if (l1.data > l2.data) {
        result.next = l2;
        l2 = l2.next;
      } else {
        result.next = l1;
        l1 = l1.next;
      }
      result = result.next;
    }
    if (l2 == null) {
      result.next = l1;
    } else {
      result.next = l2;
    }

    return dummy.next;
  }

}
