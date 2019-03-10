# Brutal Force
# c c a a b b b
# c a a b b b
# a a b b b
# a   b b
#     b
#
# 4 3 5 4 3 2 1
# return the max number from all combination
class Solution1:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = []
        for i in range(0, len(s)):
            t = {}
            t[s[i]] = s[i]
            n = 1
            for j in range(i+1, len(s)):
                if s[j] not in t.keys():
                    if len(t.keys()) == 2:
                        break
                    t[s[j]] = s[j]
                n += 1
            res.append(n)
        return max(res)

# Sliding Window
class Solution2:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        left, right = 0, 0
        t = {}
        max_len = 2
        while right < len(s):
            if len(t.keys()) < 3:
                t[s[right]] = right
                right += 1
            
            if len(t.keys()) == 3:
                # delete the leftmost character
                del_idx = min(t.values())
                del t[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len 

print(Solution2().lengthOfLongestSubstringTwoDistinct("eceba"))
# expected: 3

print(Solution2().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
# expected: 5

print(Solution2().lengthOfLongestSubstringTwoDistinct("abcabcbb"))
# expected: 4
