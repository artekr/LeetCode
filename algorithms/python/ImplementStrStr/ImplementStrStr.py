class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return 0 if not needle else -1
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j > len(haystack)-1:
                    return -1
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1

        #####
        ## More python way
        #####
#       for i in range(len(haystack) - len(needle)+1):
#           if haystack[i:i+len(needle)] == needle:
#               return i
#       return -1

assert Solution().strStr("", "a") == -1
assert Solution().strStr("a", "") == 0
assert Solution().strStr("aaa", "aaaa") == -1
assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("mississippi", "issip") == 4
assert Solution().strStr("mississippi", "issipi") == -1
assert Solution().strStr("aaaaa", "bba") == -1

print("OH YEAH!")