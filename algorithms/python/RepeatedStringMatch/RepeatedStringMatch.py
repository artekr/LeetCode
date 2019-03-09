class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 0
        counter = 1
        repeatedA = A
        while len(repeatedA) < len(B)*2:
            repeatedA += A
            if B in repeatedA:
                return counter
            counter += 1
        return -1


a = 'abc'
b = 'abcs'
if find('c', a):
    print('yes')
else:
    print('no')
# print(not a.index('s'))