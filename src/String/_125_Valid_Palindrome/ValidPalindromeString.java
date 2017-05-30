package String._125_Valid_Palindrome;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * Created by hengwang on 2017-05-29.
 *
 * Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 *
 */
public class ValidPalindromeString {

  /**
   * Using a Stack to store the reversed String with only alphanumeric characters
   * And a ArrayList to store the forward String with only alphanumeric characters
   * Then compare the two
   * @param s
   * @return
   */
  public boolean isPalindrome_Stack(String s) {

    // For the purpose of this problem, we define empty string as valid palindrome.
    if (s == "") {
      return true;
    }

    Stack<Character> charStack = new Stack<>();
    ArrayList<Character> charList = new ArrayList<>();
    s = s.toLowerCase();

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (Character.isLetterOrDigit(c)) {
        charStack.push(c);
        charList.add(c);
      }
    }

    for (int i = 0; i < charList.size(); i++) {
      char stackChar = charStack.pop();
      if (charList.get(i) != stackChar) {
        return false;
      }
    }
    // The char stack should be empty
    return charStack.empty();
  }
  // Runtime: 28 ms. Beats 23.16% java submissions.


  /**
   * Regex to clean the string, compare front and end
   * @param s
   * @return
   */
  public boolean isPalindrome_Regex(String s) {

    String regex = "([^A-Za-z0-9])";
    String replacement = "";
    s = s.replaceAll(regex, replacement).toLowerCase();

    for (int i = 0; i < s.length() / 2; i++) {
      if (s.charAt(i) != s.charAt(s.length()-1-i)) {
        return false;
      }
    }
    return true;
  }

}
