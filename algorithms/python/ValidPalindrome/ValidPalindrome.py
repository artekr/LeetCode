import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # regex '[^A-Za-z0-9]', find all characters that is not matching this pattern
        # replace findings with empty ''
        # conver the translated string to lower case
        s = re.sub('[^A-Za-z0-9]', '', s).lower()
        if not s:
            return True
        
        ## Compare start and end while substract them from string 
        # while len(s) != 1:
        #     if not s:
        #         return True
        #     if s[0] != s[len(s)-1]:
        #         return False
        #     s = s[1:len(s)-1]
        # return True

        ## Divided by half and compare start and end
        for i in range(0, len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# expected: True

print(Solution().isPalindrome("race a car"))
# expected: False

print(Solution().isPalindrome(" "))
# expected: True

print(Solution().isPalindrome("aa"))
# expected: True