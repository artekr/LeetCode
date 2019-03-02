package LinkedList._237_Delete_Node_In_A_Linked_List;

import DataStructure.ListNode;

/**
 * Created by hengwang on 2017-05-25.
 *
 * Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
 * Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
 * the linked list should become 1 -> 2 -> 4 after calling your function.
 *
 * LeetCode:
 * https://leetcode.com/problems/delete-node-in-a-linked-list
 */
public class DeleteNodeInALinkedList {

  public void deleteNode(ListNode node) {
    // No need to shuffle all the rest elements.
    node.data=node.next.data;
    node.next=node.next.next;
  }

}
