# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.val_stack = []
        self.min_stack = []
        self.max_stack = []


def peek(self):
    if len(self.val_stack) == 0:
        return None
    return self.val_stack[-1]


def pop(self):
    if len(self.val_stack) == 0:
        return None
    val = self.val_stack.pop()
    self.min_stack.pop()
    self.max_stack.pop()
    return val


def push(self, number):
    self.val_stack.append(number)
    if len(self.val_stack) == 1:
        self.min_stack.append(number)
        self.max_stack.append(number)
    else:
        self.min_stack.append(min(number, self.min_stack[-1]))
        self.max_stack.append(max(number, self.max_stack[-1]))


def getMin(self):
    if len(self.val_stack) == 0:
        return None
    return self.min_stack[-1]


def getMax(self):
    if len(self.val_stack) == 0:
        return None
    return self.max_stack[-1]
