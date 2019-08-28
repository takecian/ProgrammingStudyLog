class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue
            if len(stack) == 0:
                return False

            if stack[-1] == '(' and c == ')':
                stack.pop()
                continue
            if stack[-1] == '[' and c == ']':
                stack.pop()
                continue
            if stack[-1] == '{' and c == '}':
                stack.pop()
                continue
            return False

        return len(stack) == 0