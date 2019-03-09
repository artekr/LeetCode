class Solution1:
    def firstUniqChar(self, s: str) -> int:
        if s:
            for char in s:
                if s.count(char) == 1: # This take long time
                    return s.index(char)
        return -1

# Using hashmap
import collections
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        if s:
            count = collections.Counter(s)
            for char in s:
                if count[char] == 1:
                    return s.index(char)
        return -1

print(Solution1().firstUniqChar('leetcode'))
# expected: 0
