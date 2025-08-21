"""
String Manipulation Patterns - Common String Processing Techniques

Implementations of common string manipulation patterns for coding interviews.
"""

from typing import List, Dict
from collections import Counter, defaultdict


def reverse_string(s: List[str]) -> None:
    """Reverse string in-place."""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_words(s: str) -> str:
    """Reverse words in a string, handling multiple spaces."""
    words = [word for word in s.split() if word]
    return ' '.join(reversed(words))


def is_anagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams."""
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group strings that are anagrams of each other."""
    anagram_groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())


def longest_common_prefix(strs: List[str]) -> str:
    """Find longest common prefix among array of strings."""
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    
    for i in range(min_len):
        char = strs[0][i]
        if any(s[i] != char for s in strs):
            return strs[0][:i]
    
    return strs[0][:min_len]


def valid_palindrome(s: str) -> bool:
    """Check if string is valid palindrome (ignoring non-alphanumeric)."""
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def string_to_integer(s: str) -> int:
    """Convert string to integer (atoi implementation)."""
    if not s:
        return 0
    
    s = s.lstrip()
    if not s:
        return 0
    
    sign = 1
    start = 0
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        start = 1
    
    result = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break
        
        digit = int(s[i])
        
        if result > (2**31 - 1 - digit) // 10:
            return -2**31 if sign == -1 else 2**31 - 1
        
        result = result * 10 + digit
    
    return sign * result


def zigzag_conversion(s: str, num_rows: int) -> str:
    """Convert string to zigzag pattern and read line by line."""
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [''] * num_rows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        
        current_row += 1 if going_down else -1
    
    return ''.join(rows)


def longest_palindromic_substring(s: str) -> str:
    """Find longest palindromic substring."""
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]


def encode_decode_strings(strs: List[str]) -> str:
    """Encode list of strings into single string."""
    encoded = ""
    for s in strs:
        encoded += str(len(s)) + "#" + s
    return encoded


def decode_strings(encoded: str) -> List[str]:
    """Decode string back to list of strings."""
    decoded = []
    i = 0
    
    while i < len(encoded):
        delimiter_pos = encoded.find('#', i)
        length = int(encoded[i:delimiter_pos])
        
        start = delimiter_pos + 1
        decoded.append(encoded[start:start + length])
        
        i = start + length
    
    return decoded


def multiply_strings(num1: str, num2: str) -> str:
    """Multiply two non-negative integers represented as strings."""
    if num1 == "0" or num2 == "0":
        return "0"
    
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    
    num1, num2 = num1[::-1], num2[::-1]
    
    for i in range(m):
        for j in range(n):
            product = int(num1[i]) * int(num2[j])
            
            result[i + j] += product
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return ''.join(map(str, result[::-1]))


def word_pattern(pattern: str, s: str) -> bool:
    """Check if string follows given pattern."""
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True


def simplify_path(path: str) -> str:
    """Simplify Unix-style file path."""
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    
    return '/' + '/'.join(stack)