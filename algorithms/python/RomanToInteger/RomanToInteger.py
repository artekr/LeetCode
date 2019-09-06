class Solution:

#   I - 1
#   V - 5
#   X - 10
#   L - 50
#   C - 100
#   D - 500
#   M - 1000

#   IV - 4
#   IX - 9
#   XL - 40
#   XC - 90
#   CD - 400
#   CM - 900

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
                total -= 1
                continue
            if s[i] == "X" and (prev == "L" or prev == "C"):
                total -= 10
                continue
            if s[i] == "C" and (prev == "D" or prev == "M"):
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