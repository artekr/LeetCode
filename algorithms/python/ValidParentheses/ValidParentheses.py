class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if (a == '(' and char != ')') or (a == '{' and char != '}') or (a == '[' and char != ']'):
                    return False
        return not stack



print(Solution().isValid("(()("))
# expected: False

print(Solution().isValid("(()){[]}[{()}]"))
# expected: True

print(Solution().isValid("))"))
# expected: False
