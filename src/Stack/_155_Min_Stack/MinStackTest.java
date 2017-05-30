package Stack._155_Min_Stack;

/**
 * Created by hengwang on 2017-05-30.
 */
public class MinStackTest {

  public static void main(String[] args) {

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    System.out.println(minStack.getMin());   // --> Returns -3.
    minStack.pop();
    System.out.println(minStack.top());      // --> Returns 0.
    System.out.println(minStack.getMin());   // --> Returns -2.
  }
}
