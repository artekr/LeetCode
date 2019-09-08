class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("a ") == 1

print("OH YEAH!")
