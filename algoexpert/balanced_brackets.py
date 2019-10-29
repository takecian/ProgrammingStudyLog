def balancedBrackets(string):
    # Write your code here.
    stack = []
    opens = ['(', '{', '[']
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in opens:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0