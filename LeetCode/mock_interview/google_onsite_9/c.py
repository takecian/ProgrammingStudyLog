class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        repeat = 0
        string = ''
        for c in s:
            if c.isdigit():
                repeat = repeat * 10 + int(c)
            elif c == '[':
                stack.append(string)
                stack.append(repeat)
                string = ''
                repeat = 0
            elif c == ']':
                decoded = string * stack.pop()
                string = stack.pop() + decoded
            else:
                string += c
        return string
