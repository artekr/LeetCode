class Solution:

#   I - 1
#   V - 5
#   X - 10
#   L - 50
#   C - 100
#   D - 500
#   M - 1000

    def romanToInt(self, s: str) -> int:
        total = 0
        prev = ""
        base = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
        for i in range(len(s)-1, -1, -1):
            if s[i] == "I" and (prev == "V" or prev == "X"):
                # IV - 4
                # IX - 9
                total -= 1
                continue
            if s[i] == "X" and (prev == "L" or prev == "C"):
                # XL - 40
                # XC - 90
                total -= 10
                continue
            if s[i] == "C" and (prev == "D" or prev == "M"):
                # CD - 400
                # CM - 900
                total -= 100
                continue
            prev = s[i]
            total += base.get(s[i])
        return total


assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("LVIII") == 58
assert Solution().romanToInt("CCCXCIX") == 399
assert Solution().romanToInt("MCMXCIV") == 1994

print("OH YEAH!")