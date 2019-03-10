# Sliding Window
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return n
        
        left, right = 0, 0
        hashtable = {}
        max_len = k
        while right < n:
            if len(hashtable.keys()) < k+1:
                hashtable[s[right]] = right
                right += 1
            if len(hashtable.keys()) == k+1:
                del_index = min(hashtable.values())
                del hashtable[s[del_index]]
                left = del_index + 1
            max_len = max(max_len, right - left)
        return max_len

print(Solution().lengthOfLongestSubstringKDistinct("eceba", 2))
# expected: 3