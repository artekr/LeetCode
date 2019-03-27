
# Naive
class Solution1:
    def licenseKeyFormatting(self, S: str, K: int):
        if K >= len(S):
            return S.replace('-','').upper()
        
        n = len(S) - 1
        res = []
        s = ""
        while n >= 0:
            if len(s) < K:
                if S[n] != '-':
                    s = S[n] + s
                n -= 1
            else:
                res.append(s)
                s = ""
        if s != '-' and s != '':
            res.append(s)
        # return res
        result = ""
        for s in res:
            result = '-' + s.upper() + result
        return result[1:]


# Elegant
class Solution2:
    def licenseKeyFormatting(self, S: str, K: int):
        S = S.replace('-', '').upper()
        size = len(S)
        first = K if size % K == 0 else size % K
        res = S[:first]
        while first < size:
            res += '-' + S[first:first+K]
            first += K
        return res


print(Solution2().licenseKeyFormatting("5F3Z-2e-9-w", 4))
# expected: "5F3Z-2E9W"

print(Solution2().licenseKeyFormatting("--a-a-a-a--", 2))
# expected: "AA-AA"

print(Solution2().licenseKeyFormatting("2-5g-3-J", 2))
# expected: "2-5G-3J"

print(Solution2().licenseKeyFormatting("---", 100))
# expected: ""

        