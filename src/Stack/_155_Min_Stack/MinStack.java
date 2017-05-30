package Stack._155_Min_Stack;

import java.util.Stack;

/**
 * Created by hengwang on 2017-05-30.
 */
public class MinStack {

  int min;
  Stack<Integer> stack;

  public MinStack() {
    min = Integer.MAX_VALUE;
    stack = new Stack<>();
  }

  public void push(int x) {
    if (x <= min) {
      stack.push(min);
      min = x;
    }
    stack.push(x);
  }

  public void pop() {
    int val = stack.pop();
    if (val == min) {
      min = stack.pop();
    }
  }

  public int top() {
    return stack.peek();
  }

  public int getMin() {
    return min;
  }
}
