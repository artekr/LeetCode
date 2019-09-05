from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        for c in s:
            print(c, end = ' ')
        print()


Solution().reverseString(["h","e","l","l","o"])
# expected: ["o","l","l","e","h"]

Solution().reverseString(["H","a","n","n","a","h"])
# expected: ["h","a","n","n","a","H"]

Solution().reverseString([])
# expected: []
