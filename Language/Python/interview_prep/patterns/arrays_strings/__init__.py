"""
Array and String Manipulation Patterns

This package contains essential patterns for solving array and string problems
commonly encountered in technical interviews.

Modules:
- two_pointers: Two pointers technique for arrays and strings
- sliding_window: Sliding window pattern for subarray/substring problems
- string_manipulation: String processing and manipulation techniques
- test_patterns: Unit tests for all pattern implementations

Usage:
    from patterns.arrays_strings import TwoPointersPatterns, SlidingWindowPatterns
    from patterns.arrays_strings import StringManipulationPatterns
"""

from .two_pointers import TwoPointersPatterns
from .sliding_window import SlidingWindowPatterns
from .string_manipulation import StringManipulationPatterns, AdvancedStringPatterns

__all__ = [
    'TwoPointersPatterns',
    'SlidingWindowPatterns', 
    'StringManipulationPatterns',
    'AdvancedStringPatterns'
]