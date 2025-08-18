def is_balanced(s: str) -> bool:
    """
    Checks if the parentheses, brackets, and braces in a string are balanced.

    A string of brackets is considered valid if:
    1.  Every opening bracket `(`, `[`, or `{` has a corresponding closing bracket `)`, `]`, or `}` of the same type.
    2.  The brackets are closed in the correct order. For example, `([)]` is invalid.
    3.  Any characters that are not brackets should be ignored.

    Args:
        s: The input string.

    Returns:
        True if the brackets are balanced, False otherwise.
    """
    # The stack will store the opening brackets we encounter.
    stack = []

    # This mapping helps us quickly find the matching opening bracket for any closing bracket.
    # This is cleaner than a long if/elif/else block.
    bracket_map = {")": "(", "]": "[", "}": "{"}

    # A set for quick lookups of opening brackets.
    open_brackets = set(bracket_map.values())

    for char in s:
        # If it's an opening bracket, push it onto the stack.
        if char in open_brackets:
            stack.append(char)
        # If it's a closing bracket...
        elif char in bracket_map:
            # ...but the stack is empty, it means we have a closer with no opener.
            if not stack:
                return False
            
            # Pop the last opening bracket from the stack.
            last_open = stack.pop()

            # Check if the popped opener matches the current closer.
            if last_open != bracket_map[char]:
                return False
        # Any other character is ignored, as planned.

    # After iterating through the string, if the stack is empty, all brackets were matched.
    # If not, there are unclosed opening brackets.
    return not stack

def run_tests():
    """Runs a set of test cases for the is_balanced function."""
    test_cases = {
        "([]{Hello(), world!!})": True,
        "(Hello, [world])": True,
        "([)]": False,
        "Hello, world!!)": False,
        "{": False,
        "": True,
        "())": False,
        "[[[": False
    }

    print("Running test cases for is_balanced...")
    for test_string, expected in test_cases.items():
        result = is_balanced(test_string)
        status = "✅" if result == expected else "❌"
        print(f"{status} | Input: '{test_string}' -> Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_tests()