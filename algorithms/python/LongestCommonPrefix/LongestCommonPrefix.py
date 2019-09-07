from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = strs[0]
        for s in strs:
            length = min(len(s),len(result))
            result = result[:length]
            for i in range(length):
                if not result:
                    return ""
                if s[i] != result[i]:
                    result = result[:i]
                    break
        return result


assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""

print("OH YEAH!")
