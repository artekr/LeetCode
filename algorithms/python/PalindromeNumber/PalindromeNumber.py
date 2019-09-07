class Solution:
    def isPalindrome_reverse_number(self, x: int) -> bool:
        def reverseNumber(x):
            rev = 0
            while x != 0:
                last = x % 10
                x //= 10
                rev = rev*10 + last
            return rev

        if x < 0:
            return False
        return x == reverseNumber(x)

    def isPalindrome_reverse_half(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverseNum = 0
        while x > reverseNum:
            reverseNum = reverseNum*10 + (x % 10)
            x //= 10
        return x == reverseNum or x == (reverseNum // 10)



assert Solution().isPalindrome_reverse_half(12321) == True
assert Solution().isPalindrome_reverse_number(1231) == False
assert Solution().isPalindrome_reverse_half(-123) == False
assert Solution().isPalindrome_reverse_half(0) == True

print("OH YEAH!")
