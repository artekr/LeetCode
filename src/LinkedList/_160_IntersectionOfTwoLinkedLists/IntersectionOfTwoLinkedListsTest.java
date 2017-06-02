package LinkedList._160_IntersectionOfTwoLinkedLists;

import DataStructure.ListNode;
import DataStructure.SingleLinkedList;

/**
 * Created by hengwang on 2017-06-02.
 */
public class IntersectionOfTwoLinkedListsTest {

  public static void main(String[] args) {

    ListNode headA = new ListNode(1);
    ListNode A2 = new ListNode(2);

    ListNode headB = new ListNode(1);
    ListNode B2 = new ListNode(2);
    ListNode B3 = new ListNode(3);

    ListNode intersection = new ListNode(100);
    ListNode intersection2 = new ListNode(200);
    ListNode intersection3 = new ListNode(300);

    // Build linked list A part
    headA.next = A2;
    A2.next = intersection;

    // Build linked list B part
    headB.next = B2;
    B2.next = B3;
    B3.next = intersection;

    // Build common part
    intersection.next = intersection2;
    intersection2.next = intersection3;

    SingleLinkedList.printLinkedList(headA);
    SingleLinkedList.printLinkedList(headB);

    IntersectionOfTwoLinkedLists Test = new IntersectionOfTwoLinkedLists();
    ListNode possible_intersection = Test.getIntersectionNode(headA, headB);
    ListNode possible_intersection_solution2 = Test.getIntersectionNode_NoLengthDifference(headA, headB);
    System.out.println("Intersection: " + possible_intersection.data);  // Expected: 100
    System.out.println("Intersection solution2: " + possible_intersection_solution2.data);  // Expected: 100


    /***************************************************************/
    ListNode headA_2 = new ListNode(1);
    ListNode A2_2 = new ListNode(2);

    ListNode headB_2 = new ListNode(1);
    ListNode B2_2 = new ListNode(2);
    ListNode B3_2 = new ListNode(3);

    // Build linked list A part
    headA_2.next = A2_2;

    // Build linked list B part
    headB_2.next = B2_2;
    B2_2.next = B3_2;

    SingleLinkedList.printLinkedList(headA_2);
    SingleLinkedList.printLinkedList(headB_2);

    IntersectionOfTwoLinkedLists Test_2 = new IntersectionOfTwoLinkedLists();
    ListNode possible_intersection_2 = Test.getIntersectionNode(headA_2, headB_2);
    ListNode possible_intersection__2_solution2 = Test.getIntersectionNode_NoLengthDifference(headA, headB);
    System.out.println("Intersection: " + possible_intersection_2); // Expected: null
    System.out.println("Intersection solution2: " + possible_intersection__2_solution2); // Expected: null
  }
}
