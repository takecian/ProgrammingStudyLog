"""
Utility functions for input parsing and output formatting in coding interviews.

This module provides common utility functions that are frequently needed
during coding interviews, including input parsing, output formatting,
and helper functions for testing and debugging.
"""

import sys
from typing import List, Tuple, Any, Optional, Union, Iterator
from collections import defaultdict, Counter
import re


class InputParser:
    """Utilities for parsing different types of input formats."""
    
    @staticmethod
    def read_int() -> int:
        """Read a single integer from input."""
        return int(input().strip())
    
    @staticmethod
    def read_ints() -> List[int]:
        """Read a line of space-separated integers."""
        return list(map(int, input().split()))
    
    @staticmethod
    def read_string() -> str:
        """Read a string, stripping whitespace."""
        return input().strip()
    
    @staticmethod
    def read_strings() -> List[str]:
        """Read a line of space-separated strings."""
        return input().split()
    
    @staticmethod
    def read_matrix(rows: int, cols: Optional[int] = None) -> List[List[int]]:
        """Read a matrix of integers."""
        matrix = []
        for _ in range(rows):
            row = list(map(int, input().split()))
            if cols is not None and len(row) != cols:
                raise ValueError(f"Expected {cols} columns, got {len(row)}")
            matrix.append(row)
        return matrix
    
    @staticmethod
    def read_string_matrix(rows: int) -> List[List[str]]:
        """Read a matrix of characters/strings."""
        return [list(input().strip()) for _ in range(rows)]
    
    @staticmethod
    def read_edges(num_edges: int, one_indexed: bool = False) -> List[Tuple[int, int]]:
        """Read edge list for graph problems."""
        edges = []
        for _ in range(num_edges):
            u, v = map(int, input().split())
            if one_indexed:
                u -= 1
                v -= 1
            edges.append((u, v))
        return edges
    
    @staticmethod
    def read_weighted_edges(num_edges: int, one_indexed: bool = False) -> List[Tuple[int, int, int]]:
        """Read weighted edge list for graph problems."""
        edges = []
        for _ in range(num_edges):
            u, v, w = map(int, input().split())
            if one_indexed:
                u -= 1
                v -= 1
            edges.append((u, v, w))
        return edges
    
    @staticmethod
    def read_test_cases() -> Iterator[int]:
        """Read number of test cases and yield each case number."""
        t = int(input())
        for case_num in range(1, t + 1):
            yield case_num
    
    @staticmethod
    def parse_coordinate(coord_str: str) -> Tuple[int, int]:
        """Parse coordinate string like '(3,4)' or '3,4'."""
        # Remove parentheses and split by comma
        clean_str = coord_str.strip('()')
        x, y = map(int, clean_str.split(','))
        return (x, y)
    
    @staticmethod
    def parse_range(range_str: str) -> Tuple[int, int]:
        """Parse range string like '1-5' or '1..5'."""
        if '-' in range_str:
            start, end = map(int, range_str.split('-'))
        elif '..' in range_str:
            start, end = map(int, range_str.split('..'))
        else:
            raise ValueError(f"Invalid range format: {range_str}")
        return (start, end)


class OutputFormatter:
    """Utilities for formatting output in different styles."""
    
    @staticmethod
    def print_list(lst: List[Any], separator: str = ' ') -> None:
        """Print list elements separated by given separator."""
        print(separator.join(map(str, lst)))
    
    @staticmethod
    def print_matrix(matrix: List[List[Any]], row_separator: str = '\n', col_separator: str = ' ') -> None:
        """Print matrix with custom separators."""
        for row in matrix:
            print(col_separator.join(map(str, row)))
    
    @staticmethod
    def print_yes_no(condition: bool, yes: str = "YES", no: str = "NO") -> None:
        """Print YES/NO based on condition."""
        print(yes if condition else no)
    
    @staticmethod
    def print_case_result(case_num: int, result: Any) -> None:
        """Print result in 'Case #X: result' format."""
        print(f"Case #{case_num}: {result}")
    
    @staticmethod
    def format_float(value: float, precision: int = 6) -> str:
        """Format float with specified precision."""
        return f"{value:.{precision}f}"
    
    @staticmethod
    def format_percentage(value: float, precision: int = 2) -> str:
        """Format value as percentage."""
        return f"{value * 100:.{precision}f}%"
    
    @staticmethod
    def format_time(seconds: float) -> str:
        """Format time in human-readable format."""
        if seconds < 1:
            return f"{seconds * 1000:.1f}ms"
        elif seconds < 60:
            return f"{seconds:.2f}s"
        else:
            minutes = int(seconds // 60)
            remaining_seconds = seconds % 60
            return f"{minutes}m {remaining_seconds:.1f}s"


class TestingUtils:
    """Utilities for testing and debugging solutions."""
    
    @staticmethod
    def time_function(func, *args, **kwargs):
        """Time the execution of a function."""
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    
    @staticmethod
    def compare_outputs(expected: Any, actual: Any, tolerance: float = 1e-9) -> bool:
        """Compare expected and actual outputs with tolerance for floats."""
        if isinstance(expected, float) and isinstance(actual, float):
            return abs(expected - actual) <= tolerance
        elif isinstance(expected, list) and isinstance(actual, list):
            if len(expected) != len(actual):
                return False
            return all(TestingUtils.compare_outputs(e, a, tolerance) 
                      for e, a in zip(expected, actual))
        else:
            return expected == actual
    
    @staticmethod
    def generate_test_case(func, inputs: List[Any], expected_output: Any) -> dict:
        """Generate a test case dictionary."""
        return {
            'inputs': inputs,
            'expected': expected_output,
            'function': func
        }
    
    @staticmethod
    def run_test_cases(test_cases: List[dict], verbose: bool = True) -> Tuple[int, int]:
        """Run multiple test cases and return (passed, total)."""
        passed = 0
        total = len(test_cases)
        
        for i, test_case in enumerate(test_cases, 1):
            func = test_case['function']
            inputs = test_case['inputs']
            expected = test_case['expected']
            
            try:
                if isinstance(inputs, list):
                    actual = func(*inputs)
                else:
                    actual = func(inputs)
                
                if TestingUtils.compare_outputs(expected, actual):
                    passed += 1
                    if verbose:
                        print(f"Test {i}: PASSED")
                else:
                    if verbose:
                        print(f"Test {i}: FAILED")
                        print(f"  Expected: {expected}")
                        print(f"  Actual: {actual}")
            except Exception as e:
                if verbose:
                    print(f"Test {i}: ERROR - {e}")
        
        if verbose:
            print(f"\nResults: {passed}/{total} tests passed")
        
        return passed, total
    
    @staticmethod
    def debug_print(*args, enabled: bool = True) -> None:
        """Print debug information only if enabled."""
        if enabled:
            print("DEBUG:", *args, file=sys.stderr)
    
    @staticmethod
    def trace_function(func):
        """Decorator to trace function calls."""
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper


class DataStructureHelpers:
    """Helper functions for common data structure operations."""
    
    @staticmethod
    def build_adjacency_list(edges: List[Tuple[int, int]], directed: bool = False, 
                           one_indexed: bool = False) -> defaultdict:
        """Build adjacency list from edge list."""
        graph = defaultdict(list)
        for u, v in edges:
            if one_indexed:
                u -= 1
                v -= 1
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
        return graph
    
    @staticmethod
    def build_adjacency_matrix(n: int, edges: List[Tuple[int, int]], 
                             directed: bool = False, one_indexed: bool = False) -> List[List[int]]:
        """Build adjacency matrix from edge list."""
        matrix = [[0] * n for _ in range(n)]
        for u, v in edges:
            if one_indexed:
                u -= 1
                v -= 1
            matrix[u][v] = 1
            if not directed:
                matrix[v][u] = 1
        return matrix
    
    @staticmethod
    def create_prefix_sum(arr: List[int]) -> List[int]:
        """Create prefix sum array."""
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        return prefix
    
    @staticmethod
    def range_sum(prefix: List[int], left: int, right: int) -> int:
        """Get sum of range [left, right] using prefix sum."""
        return prefix[right + 1] - prefix[left]
    
    @staticmethod
    def create_2d_prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
        """Create 2D prefix sum array."""
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] = (matrix[i-1][j-1] + 
                              prefix[i-1][j] + 
                              prefix[i][j-1] - 
                              prefix[i-1][j-1])
        return prefix
    
    @staticmethod
    def range_sum_2d(prefix: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
        """Get sum of 2D range using 2D prefix sum."""
        return (prefix[r2+1][c2+1] - 
                prefix[r1][c2+1] - 
                prefix[r2+1][c1] + 
                prefix[r1][c1])


class StringHelpers:
    """Helper functions for string processing."""
    
    @staticmethod
    def is_palindrome(s: str, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool:
        """Check if string is palindrome."""
        if ignore_non_alnum:
            s = ''.join(c for c in s if c.isalnum())
        if ignore_case:
            s = s.lower()
        return s == s[::-1]
    
    @staticmethod
    def get_char_frequency(s: str) -> Counter:
        """Get character frequency counter."""
        return Counter(s)
    
    @staticmethod
    def are_anagrams(s1: str, s2: str) -> bool:
        """Check if two strings are anagrams."""
        return Counter(s1) == Counter(s2)
    
    @staticmethod
    def longest_common_prefix(strings: List[str]) -> str:
        """Find longest common prefix of strings."""
        if not strings:
            return ""
        
        min_len = min(len(s) for s in strings)
        for i in range(min_len):
            char = strings[0][i]
            if not all(s[i] == char for s in strings):
                return strings[0][:i]
        
        return strings[0][:min_len]
    
    @staticmethod
    def reverse_words(s: str) -> str:
        """Reverse words in string."""
        return ' '.join(s.split()[::-1])
    
    @staticmethod
    def remove_duplicates(s: str, keep_order: bool = True) -> str:
        """Remove duplicate characters from string."""
        if keep_order:
            seen = set()
            result = []
            for char in s:
                if char not in seen:
                    seen.add(char)
                    result.append(char)
            return ''.join(result)
        else:
            return ''.join(set(s))


class MathHelpers:
    """Helper functions for mathematical operations."""
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Greatest common divisor using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Least common multiple."""
        return abs(a * b) // MathHelpers.gcd(a, b)
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Get prime factors of number."""
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    @staticmethod
    def power_mod(base: int, exp: int, mod: int) -> int:
        """Fast modular exponentiation."""
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp = exp >> 1
            base = (base * base) % mod
        return result
    
    @staticmethod
    def factorial_mod(n: int, mod: int) -> int:
        """Factorial modulo m."""
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % mod
        return result


def demonstrate_utils():
    """Demonstrate utility functions."""
    print("=== INPUT PARSING DEMO ===")
    # Simulate reading from string input
    import io
    import sys
    
    # Mock input
    test_input = "3\n1 2 3\n4 5 6\n7 8 9\n"
    sys.stdin = io.StringIO(test_input)
    
    rows = InputParser.read_int()
    matrix = InputParser.read_matrix(rows)
    print(f"Read {rows}x{len(matrix[0])} matrix:")
    OutputFormatter.print_matrix(matrix)
    
    print("\n=== STRING HELPERS DEMO ===")
    print(f"Is 'racecar' palindrome? {StringHelpers.is_palindrome('racecar')}")
    print(f"Are 'listen' and 'silent' anagrams? {StringHelpers.are_anagrams('listen', 'silent')}")
    
    print("\n=== MATH HELPERS DEMO ===")
    print(f"GCD of 48 and 18: {MathHelpers.gcd(48, 18)}")
    print(f"Is 17 prime? {MathHelpers.is_prime(17)}")
    print(f"Prime factors of 60: {MathHelpers.prime_factors(60)}")


if __name__ == "__main__":
    demonstrate_utils()