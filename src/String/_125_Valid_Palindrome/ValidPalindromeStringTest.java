package String._125_Valid_Palindrome;

/**
 * Created by hengwang on 2017-05-29.
 */
public class ValidPalindromeStringTest {
  public static void main(String[] args) {

    String s1 = "A man, a plan, a canal: Panama";
    String s2 = "race a car";
    String s3 = "Tac4 A 4cat";
    String s4 = "Tac4 A 4cats";

    ValidPalindromeString Test = new ValidPalindromeString();
    System.out.println(Test.isPalindrome_Stack(s1)); // Expected: true
    System.out.println(Test.isPalindrome_Stack(s2)); // Expected: false

    System.out.println(Test.isPalindrome_Regex(s3)); // Expected: true
    System.out.println(Test.isPalindrome_Regex(s4)); // Expected: false

  }
}
