# Dynamic Programming
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        first = 1
        second = 0 if s[0] == '0' else 1
        for i in range(0, len(s)-1):    
            current = 0
            if 10 <= int(s[i:i+2]) < 27:
                current += first
            if int(s[i+1]) != 0:
                current += second 
            first = second
            second = current

        return second


print(Solution().numDecodings("100"))
# expected: 0

# print(Solution().numDecodings("1"))
# # expected: 1

# print(Solution().numDecodings("00"))
# # expected: 0

# print(Solution().numDecodings("01"))
# # expected: 0

# print(Solution().numDecodings("12"))
# # expected: 2

# print(Solution().numDecodings("100"))
# # expected: 0

# print(Solution().numDecodings("101"))
# # expected: 1

# print(Solution().numDecodings("226"))
# # # expected: 3

# print(Solution().numDecodings("110"))
# expected: 1