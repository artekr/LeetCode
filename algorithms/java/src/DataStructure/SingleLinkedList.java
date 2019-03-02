package DataStructure;

import DataStructure.ListNode;

public class SingleLinkedList {

  public ListNode head;
  public int listCount;

  public SingleLinkedList() {
    listCount = 0;
  }

  public void printList() {

  }

  /**
   * Given the head of Linked List, print all the elements
   * @param head
   */
  public static void printLinkedList(ListNode head) {
    while (head != null) {
      System.out.print(head.data);
      if (head.next != null) {
        System.out.print("->");
      }
      head = head.next;
    }
    System.out.println();
  }

  /**
   * Get the length of the linked list
   * @return Length of the linked list
   */
  public int length() {
    return listCount;
  }

  /**
   * Append a node to tail
   * @param node
   */
  public void add(ListNode node) {

    if (head == null) {
      head = node;
    }

    ListNode current = head;

    while (current.next != null) {
      current = current.next;
    }
    current.next = node;
    listCount++;
  }

  /**
   * Insert a node at index
   * @param node
   * @param index
   */
  public void insert(ListNode node, int index) {

    ListNode current = head;
    int count = 0;

    if (index > listCount || index < 1) {
      System.out.println("Add Failed: index out of bounds of size of linked list!!");
    } else {

      if (current != null) {
        while (count < index - 1) {
          current = current.next;
          count++;
        }

        node.next = current.next;
        current.next = node;
        listCount++;
      }
    }
  }

  /**
   * Delete a node
   * @param node
   */
  public boolean deleteNode(ListNode node) {

    ListNode current = head;
    while (current.next != null) {

      if (current.next == node) {
        current.next = null;
        listCount--;
        return true;
      }
      current = current.next;
    }
    return false;
  }


  /**
   * Delete a node at given index
   * @param index
   */
  public boolean deletedNodeAtIndex(int index) {

    ListNode current = head;
    int count = 0;

    if (index > listCount || index < 1) {
      System.out.println("Delete Failed: index out of bounds of size of linked list!!");
      return false;
    }

    while (count < index - 1) {
      count++;
      current = current.next;
    }

    current.next = current.next.next;
    listCount--;
    return true;
  }


}