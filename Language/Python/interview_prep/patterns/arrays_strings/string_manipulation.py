"""
<<<<<<< HEAD
String Manipulation Patterns for Technical Interviews

This module covers essential string processing techniques commonly used in coding interviews.
These patterns focus on efficient string operations, parsing, and transformation using
Python's built-in string methods and advanced techniques.

Common use cases:
- String parsing and validation
- Pattern matching and searching
- String transformation and formatting
- Palindrome and anagram problems
- Substring and subsequence problems
"""

from typing import List, Dict, Set, Optional, Tuple
=======
String Manipulation Patterns - Common String Processing Techniques

This module contains implementations of common string manipulation patterns
frequently encountered in coding interviews.

Common Use Cases:
- String parsing and validation
- Pattern matching and searching
- String transformation and encoding
- Substring operations
- Character frequency analysis
"""

from typing import List, Dict, Set, Optional
>>>>>>> 173ecd5 (wip)
from collections import Counter, defaultdict
import re


<<<<<<< HEAD
class StringManipulationPatterns:
    """Collection of string manipulation patterns and techniques."""
    
    @staticmethod
    def is_anagram(s1: str, s2: str) -> bool:
        """
        Check if two strings are anagrams.
        
        Time: O(n), Space: O(1) - at most 26 characters
        
        Template for: Anagram detection, character frequency comparison
        """
        if len(s1) != len(s2):
            return False
        
        # Method 1: Using Counter (most Pythonic)
        return Counter(s1) == Counter(s2)
        
        # Method 2: Using sorting
        # return sorted(s1) == sorted(s2)
        
        # Method 3: Manual counting
        # char_count = defaultdict(int)
        # for char in s1:
        #     char_count[char] += 1
        # for char in s2:
        #     char_count[char] -= 1
        # return all(count == 0 for count in char_count.values())
    
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        """
        Group strings that are anagrams of each other.
        
        Time: O(n * k log k), Space: O(n * k)
        where n = number of strings, k = max string length
        
        Template for: Grouping by pattern, hash key generation
        """
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Use sorted string as key
            key = ''.join(sorted(s))
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())
    
    @staticmethod
    def longest_palindromic_substring(s: str) -> str:
        """
        Find the longest palindromic substring.
        
        Time: O(n²), Space: O(1)
        
        Template for: Palindrome detection, expand around center
        """
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand_around_center(left: int, right: int) -> int:
            """Expand around center and return length of palindrome."""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center at i)
            len1 = expand_around_center(i, i)
            # Check for even-length palindromes (center between i and i+1)
            len2 = expand_around_center(i, i + 1)
            
            current_max = max(len1, len2)
            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2
        
        return s[start:start + max_len]
    
    @staticmethod
    def string_compression(s: str) -> str:
        """
        Compress string using character counts (e.g., "aabcccccaaa" -> "a2b1c5a3").
        
        Time: O(n), Space: O(1) excluding output
        
        Template for: String encoding, run-length encoding
        """
        if not s:
            return ""
        
        compressed = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                compressed.append(s[i - 1] + str(count))
                count = 1
        
        # Add last group
        compressed.append(s[-1] + str(count))
        
        result = ''.join(compressed)
        return result if len(result) < len(s) else s
    
    @staticmethod
    def valid_parentheses(s: str) -> bool:
        """
        Check if parentheses are valid and properly nested.
        
        Time: O(n), Space: O(n)
        
        Template for: Stack-based validation, bracket matching
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # Opening bracket
                stack.append(char)
        
        return not stack
    
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        """
        Find longest common prefix among array of strings.
        
        Time: O(S) where S is sum of all characters, Space: O(1)
        
        Template for: Prefix matching, string comparison
        """
        if not strs:
            return ""
        
        # Method 1: Vertical scanning
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]
    
    @staticmethod
    def reverse_words(s: str) -> str:
        """
        Reverse words in a string, handling extra spaces.
        
        Time: O(n), Space: O(n)
        
        Template for: String parsing, word manipulation
        """
        # Method 1: Using built-in methods (most Pythonic)
        return ' '.join(s.split()[::-1])
        
        # Method 2: Manual parsing
        # words = []
        # word = []
        # 
        # for char in s + ' ':  # Add space to handle last word
        #     if char != ' ':
        #         word.append(char)
        #     elif word:
        #         words.append(''.join(word))
        #         word = []
        # 
        # return ' '.join(reversed(words))
    
    @staticmethod
    def string_to_integer_atoi(s: str) -> int:
        """
        Convert string to integer with proper handling of edge cases.
        
        Time: O(n), Space: O(1)
        
        Template for: String parsing, number conversion
        """
        if not s:
            return 0
        
        # Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Check sign
        sign = 1
        start_idx = 0
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            start_idx = 1
        
        # Convert digits
        result = 0
        for i in range(start_idx, len(s)):
            if not s[i].isdigit():
                break
            
            digit = int(s[i])
            
            # Check for overflow
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
        
        return sign * result
    
    @staticmethod
    def find_all_substrings(s: str, pattern: str) -> List[int]:
        """
        Find all starting indices of pattern in string.
        
        Time: O(n * m), Space: O(1)
        
        Template for: Pattern matching, substring search
        """
        indices = []
        
        for i in range(len(s) - len(pattern) + 1):
            if s[i:i + len(pattern)] == pattern:
                indices.append(i)
        
        return indices
    
    @staticmethod
    def remove_duplicates_from_string(s: str) -> str:
        """
        Remove duplicate characters while preserving order.
        
        Time: O(n), Space: O(n)
        
        Template for: Deduplication, order preservation
        """
        seen = set()
        result = []
        
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        
        return ''.join(result)
    
    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        """
        Check if s is a subsequence of t.
        
        Time: O(n), Space: O(1)
        
        Template for: Subsequence matching, two pointers
        """
        s_idx = 0
        
        for char in t:
            if s_idx < len(s) and char == s[s_idx]:
                s_idx += 1
        
        return s_idx == len(s)


class AdvancedStringPatterns:
    """Advanced string manipulation techniques."""
    
    @staticmethod
    def kmp_search(text: str, pattern: str) -> List[int]:
        """
        KMP (Knuth-Morris-Pratt) pattern searching algorithm.
        
        Time: O(n + m), Space: O(m)
        
        Template for: Efficient pattern matching
        """
        def build_lps_array(pattern: str) -> List[int]:
            """Build Longest Proper Prefix which is also Suffix array."""
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            
            return lps
        
        if not pattern:
            return []
        
        lps = build_lps_array(pattern)
        indices = []
        
        i = j = 0  # i for text, j for pattern
        
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == len(pattern):
                indices.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return indices
    
    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """
        Calculate minimum edit distance between two strings.
        
        Time: O(m * n), Space: O(m * n)
        
        Template for: Dynamic programming on strings
        """
        m, n = len(word1), len(word2)
        
        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # Delete
                        dp[i][j - 1],      # Insert
                        dp[i - 1][j - 1]   # Replace
                    )
        
        return dp[m][n]


# Python-specific string utilities
class PythonStringUtils:
    """Python-specific string manipulation utilities."""
    
    @staticmethod
    def string_formatting_examples():
        """Examples of Python string formatting techniques."""
        name = "Alice"
        age = 30
        score = 95.67
        
        # f-strings (Python 3.6+) - most preferred
        result1 = f"Name: {name}, Age: {age}, Score: {score:.2f}"
        
        # str.format() method
        result2 = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
        
        # % formatting (older style)
        result3 = "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
        
        return [result1, result2, result3]
    
    @staticmethod
    def regex_patterns():
        """Common regex patterns for interviews."""
        patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone': r'^\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$',
            'ip_address': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            'url': r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$'
        }
        return patterns
    
    @staticmethod
    def string_methods_cheatsheet():
        """Commonly used string methods in interviews."""
        s = "  Hello World  "
        
        methods = {
            'strip': s.strip(),                    # "Hello World"
            'split': s.strip().split(),            # ["Hello", "World"]
            'join': '-'.join(['a', 'b', 'c']),     # "a-b-c"
            'replace': s.replace('World', 'Python'), # "  Hello Python  "
            'find': s.find('World'),               # 8 (index of first occurrence)
            'count': s.count('l'),                 # 3
            'startswith': s.strip().startswith('Hello'),  # True
            'endswith': s.strip().endswith('World'),      # True
            'isdigit': '123'.isdigit(),            # True
            'isalpha': 'abc'.isalpha(),            # True
            'isalnum': 'abc123'.isalnum(),         # True
            'upper': s.upper(),                    # "  HELLO WORLD  "
            'lower': s.lower(),                    # "  hello world  "
            'title': s.title(),                    # "  Hello World  "
        }
        return methods


# Interview tips and common patterns
"""
String Manipulation Interview Tips:

1. **Python string advantages:**
   - Immutable (thread-safe)
   - Rich built-in methods
   - Unicode support
   - Powerful slicing: s[start:end:step]

2. **Common patterns:**
   - Two pointers for palindromes
   - Sliding window for substrings
   - Stack for bracket matching
   - Hash maps for anagrams
   - DP for edit distance

3. **Key string methods:**
   - split(), join(), strip()
   - find(), replace(), count()
   - startswith(), endswith()
   - isdigit(), isalpha(), isalnum()

4. **Performance considerations:**
   - String concatenation: use join() for multiple strings
   - String building: use list and join() instead of +=
   - Pattern matching: consider regex for complex patterns

5. **Edge cases:**
   - Empty strings
   - Single character strings
   - Strings with special characters
   - Unicode considerations
   - Case sensitivity

6. **Common mistakes:**
   - Forgetting string immutability
   - Not handling edge cases
   - Inefficient string concatenation
   - Not considering Unicode/encoding

7. **Interview-specific tips:**
   - Ask about case sensitivity
   - Clarify input constraints
   - Consider space/time trade-offs
   - Use appropriate data structures (set, dict)
=======
def reverse_string(s: List[str]) -> None:
    """
    Reverse string in-place.
    
    Args:
        s: List of characters to reverse
        
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_words(s: str) -> str:
    """
    Reverse words in a string, handling multiple spaces.
    
    Args:
        s: Input string with words separated by spaces
        
    Returns:
        String with words reversed and extra spaces removed
        
    Time: O(n), Space: O(n)
    """
    # Split by whitespace and filter empty strings
    words = [word for word in s.split() if word]
    return ' '.join(reversed(words))


def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if strings are anagrams, False otherwise
        
    Time: O(n), Space: O(1) - at most 26 characters
    """
    if len(s) != len(t):
        return False
    
    return Counter(s) == Counter(t)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.
    
    Args:
        strs: List of strings
        
    Returns:
        List of groups, where each group contains anagrams
        
    Time: O(n * k log k) where k is max string length
    Space: O(n * k)
    """
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())


def longest_common_prefix(strs: List[str]) -> str:
    """
    Find longest common prefix among array of strings.
    
    Args:
        strs: Array of strings
        
    Returns:
        Longest common prefix
        
    Time: O(S) where S is sum of all characters
    Space: O(1)
    """
    if not strs:
        return ""
    
    # Find minimum length
    min_len = min(len(s) for s in strs)
    
    for i in range(min_len):
        char = strs[0][i]
        if any(s[i] != char for s in strs):
            return strs[0][:i]
    
    return strs[0][:min_len]


def valid_palindrome(s: str) -> bool:
    """
    Check if string is valid palindrome (ignoring non-alphanumeric).
    
    Args:
        s: Input string
        
    Returns:
        True if valid palindrome, False otherwise
        
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def string_to_integer(s: str) -> int:
    """
    Convert string to integer (atoi implementation).
    
    Args:
        s: String representation of integer
        
    Returns:
        Integer value, clamped to 32-bit signed integer range
        
    Time: O(n), Space: O(1)
    """
    if not s:
        return 0
    
    # Remove leading whitespace
    s = s.lstrip()
    if not s:
        return 0
    
    # Check sign
    sign = 1
    start = 0
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        start = 1
    
    # Convert digits
    result = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break
        
        digit = int(s[i])
        
        # Check for overflow
        if result > (2**31 - 1 - digit) // 10:
            return -2**31 if sign == -1 else 2**31 - 1
        
        result = result * 10 + digit
    
    return sign * result


def zigzag_conversion(s: str, num_rows: int) -> str:
    """
    Convert string to zigzag pattern and read line by line.
    
    Args:
        s: Input string
        num_rows: Number of rows in zigzag
        
    Returns:
        String read line by line from zigzag pattern
        
    Time: O(n), Space: O(n)
    """
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [''] * num_rows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        
        # Change direction at top or bottom
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        
        current_row += 1 if going_down else -1
    
    return ''.join(rows)


def longest_palindromic_substring(s: str) -> str:
    """
    Find longest palindromic substring.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
        
    Time: O(n²), Space: O(1)
    """
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
        # Check for odd-length palindromes
        len1 = expand_around_center(i, i)
        # Check for even-length palindromes
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]


def encode_decode_strings(strs: List[str]) -> str:
    """
    Encode list of strings into single string.
    
    Args:
        strs: List of strings to encode
        
    Returns:
        Encoded string
        
    Time: O(n), Space: O(n)
    """
    encoded = ""
    for s in strs:
        # Format: length + delimiter + string
        encoded += str(len(s)) + "#" + s
    return encoded


def decode_strings(encoded: str) -> List[str]:
    """
    Decode string back to list of strings.
    
    Args:
        encoded: Encoded string
        
    Returns:
        List of decoded strings
        
    Time: O(n), Space: O(n)
    """
    decoded = []
    i = 0
    
    while i < len(encoded):
        # Find delimiter
        delimiter_pos = encoded.find('#', i)
        length = int(encoded[i:delimiter_pos])
        
        # Extract string
        start = delimiter_pos + 1
        decoded.append(encoded[start:start + length])
        
        i = start + length
    
    return decoded


def multiply_strings(num1: str, num2: str) -> str:
    """
    Multiply two non-negative integers represented as strings.
    
    Args:
        num1: First number as string
        num2: Second number as string
        
    Returns:
        Product as string
        
    Time: O(m * n), Space: O(m + n)
    """
    if num1 == "0" or num2 == "0":
        return "0"
    
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    
    # Reverse both numbers for easier calculation
    num1, num2 = num1[::-1], num2[::-1]
    
    for i in range(m):
        for j in range(n):
            # Multiply digits
            product = int(num1[i]) * int(num2[j])
            
            # Add to result
            result[i + j] += product
            
            # Handle carry
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Remove leading zeros and reverse
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return ''.join(map(str, result[::-1]))


def word_pattern(pattern: str, s: str) -> bool:
    """
    Check if string follows given pattern.
    
    Args:
        pattern: Pattern string (e.g., "abba")
        s: String to check (e.g., "dog cat cat dog")
        
    Returns:
        True if string follows pattern, False otherwise
        
    Time: O(n), Space: O(n)
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        # Check char -> word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        # Check word -> char mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True


def simplify_path(path: str) -> str:
    """
    Simplify Unix-style file path.
    
    Args:
        path: Unix file path
        
    Returns:
        Simplified canonical path
        
    Time: O(n), Space: O(n)
    """
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            # Skip empty and current directory
            continue
        elif component == '..':
            # Go to parent directory
            if stack:
                stack.pop()
        else:
            # Regular directory name
            stack.append(component)
    
    return '/' + '/'.join(stack)


# Python String Utilities for Interviews
def string_utilities():
    """
    Common Python string methods useful in interviews.
    """
    examples = {
        # Basic operations
        'split': "hello world".split(),  # ['hello', 'world']
        'join': " ".join(['hello', 'world']),  # 'hello world'
        'strip': "  hello  ".strip(),  # 'hello'
        
        # Case operations
        'lower': "Hello".lower(),  # 'hello'
        'upper': "hello".upper(),  # 'HELLO'
        'title': "hello world".title(),  # 'Hello World'
        
        # Character checks
        'isalnum': "abc123".isalnum(),  # True
        'isdigit': "123".isdigit(),  # True
        'isalpha': "abc".isalpha(),  # True
        
        # Search operations
        'find': "hello".find('l'),  # 2 (first occurrence)
        'count': "hello".count('l'),  # 2
        'startswith': "hello".startswith('he'),  # True
        'endswith': "hello".endswith('lo'),  # True
        
        # Replace operations
        'replace': "hello".replace('l', 'x'),  # 'hexxo'
        
        # Formatting
        'format': "Hello {}".format("world"),  # 'Hello world'
        'f_string': f"Hello {'world'}",  # 'Hello world'
    }
    return examples


# Interview Tips and Common Patterns
"""
String Manipulation Interview Tips:

1. **Python String Advantages**:
   - Rich built-in methods (split, join, strip, etc.)
   - Easy character iteration and slicing
   - Powerful string formatting options
   - Regular expression support

2. **Common Patterns**:
   - Two pointers for palindromes and reversals
   - Hash maps for character frequency
   - Stack for parentheses and path problems
   - Sliding window for substring problems

3. **Key Techniques**:
   - Use collections.Counter for frequency counting
   - Leverage string methods like split() and join()
   - Consider ASCII values for character operations
   - Use enumerate() for index tracking

4. **Performance Considerations**:
   - Strings are immutable in Python
   - Use list for character manipulation, join for result
   - StringBuilder pattern: chars = []; chars.append(c); ''.join(chars)
   - Avoid repeated string concatenation in loops

5. **Common Mistakes**:
   - Forgetting string immutability
   - Not handling edge cases (empty strings, single characters)
   - Case sensitivity issues
   - Unicode vs ASCII considerations

6. **Useful Built-ins**:
   - ord(c): character to ASCII
   - chr(n): ASCII to character
   - str.translate(): character mapping
   - re module for complex pattern matching
>>>>>>> 173ecd5 (wip)
"""