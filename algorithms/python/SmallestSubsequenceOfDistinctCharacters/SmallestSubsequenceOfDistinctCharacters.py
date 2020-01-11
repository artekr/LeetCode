
##########
# !!! What does `lexicographically smallest subsequence` mean??
#########

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        if not text:
            return ""
        charSet = {}
        for c in text:
            if c not in charSet:
                charSet[c] = c
        result = ""
        for c in sorted(charSet.keys()):
            result += c
        print(result)
        return result
        
# Solution().smallestSubsequence("cdadabcc")
assert Solution().smallestSubsequence("") == ""
assert Solution().smallestSubsequence("cdadabcc") == "adbc"
assert Solution().smallestSubsequence("abcd") == "abcd"
assert Solution().smallestSubsequence("ecbacba") == "eacb"
assert Solution().smallestSubsequence("leetcode") == "letcod"

print("OH YEAH!")