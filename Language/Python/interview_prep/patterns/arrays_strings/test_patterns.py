"""
Unit tests for array and string manipulation patterns.

These tests verify the correctness of pattern implementations and serve as
examples of how to use each pattern in different scenarios.
"""

import unittest
from typing import List

from .two_pointers import TwoPointersPatterns
from .sliding_window import SlidingWindowPatterns
from .string_manipulation import StringManipulationPatterns, AdvancedStringPatterns


class TestTwoPointersPatterns(unittest.TestCase):
    """Test cases for two pointers patterns."""
    
    def test_two_sum_sorted(self):
        """Test two sum in sorted array."""
        # Test case 1: Normal case
        nums = [2, 7, 11, 15]
        target = 9
        result = TwoPointersPatterns.two_sum_sorted(nums, target)
        self.assertEqual(result, (0, 1))
        
        # Test case 2: No solution
        nums = [1, 2, 3, 4]
        target = 10
        result = TwoPointersPatterns.two_sum_sorted(nums, target)
        self.assertIsNone(result)
        
        # Test case 3: Edge case - two elements
        nums = [1, 2]
        target = 3
        result = TwoPointersPatterns.two_sum_sorted(nums, target)
        self.assertEqual(result, (0, 1))
    
    def test_is_palindrome(self):
        """Test palindrome checking."""
        # Test case 1: Valid palindrome
        self.assertTrue(TwoPointersPatterns.is_palindrome("A man, a plan, a canal: Panama"))
        
        # Test case 2: Not a palindrome
        self.assertFalse(TwoPointersPatterns.is_palindrome("race a car"))
        
        # Test case 3: Empty string
        self.assertTrue(TwoPointersPatterns.is_palindrome(""))
        
        # Test case 4: Single character
        self.assertTrue(TwoPointersPatterns.is_palindrome("a"))
    
    def test_remove_duplicates(self):
        """Test removing duplicates from sorted array."""
        # Test case 1: Normal case
        nums = [1, 1, 2]
        length = TwoPointersPatterns.remove_duplicates(nums)
        self.assertEqual(length, 2)
        self.assertEqual(nums[:length], [1, 2])
        
        # Test case 2: All duplicates
        nums = [1, 1, 1, 1]
        length = TwoPointersPatterns.remove_duplicates(nums)
        self.assertEqual(length, 1)
        self.assertEqual(nums[:length], [1])
        
        # Test case 3: No duplicates
        nums = [1, 2, 3, 4]
        length = TwoPointersPatterns.remove_duplicates(nums)
        self.assertEqual(length, 4)
        self.assertEqual(nums[:length], [1, 2, 3, 4])
    
    def test_three_sum(self):
        """Test three sum problem."""
        # Test case 1: Multiple solutions
        nums = [-1, 0, 1, 2, -1, -4]
        result = TwoPointersPatterns.three_sum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(result), sorted(expected))
        
        # Test case 2: No solution
        nums = [1, 2, 3]
        result = TwoPointersPatterns.three_sum(nums)
        self.assertEqual(result, [])
        
        # Test case 3: All zeros
        nums = [0, 0, 0]
        result = TwoPointersPatterns.three_sum(nums)
        self.assertEqual(result, [[0, 0, 0]])
    
    def test_container_with_most_water(self):
        """Test container with most water."""
        # Test case 1: Normal case
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = TwoPointersPatterns.container_with_most_water(heights)
        self.assertEqual(result, 49)
        
        # Test case 2: Two elements
        heights = [1, 1]
        result = TwoPointersPatterns.container_with_most_water(heights)
        self.assertEqual(result, 1)


class TestSlidingWindowPatterns(unittest.TestCase):
    """Test cases for sliding window patterns."""
    
    def test_max_sum_subarray_fixed_size(self):
        """Test maximum sum subarray with fixed size."""
        # Test case 1: Normal case
        nums = [2, 1, 5, 1, 3, 2]
        k = 3
        result = SlidingWindowPatterns.max_sum_subarray_fixed_size(nums, k)
        self.assertEqual(result, 9)  # [5, 1, 3]
        
        # Test case 2: k equals array length
        nums = [1, 2, 3]
        k = 3
        result = SlidingWindowPatterns.max_sum_subarray_fixed_size(nums, k)
        self.assertEqual(result, 6)
        
        # Test case 3: k larger than array
        nums = [1, 2]
        k = 3
        result = SlidingWindowPatterns.max_sum_subarray_fixed_size(nums, k)
        self.assertEqual(result, 0)
    
    def test_longest_substring_without_repeating(self):
        """Test longest substring without repeating characters."""
        # Test case 1: Normal case
        s = "abcabcbb"
        result = SlidingWindowPatterns.longest_substring_without_repeating(s)
        self.assertEqual(result, 3)  # "abc"
        
        # Test case 2: All same characters
        s = "bbbbb"
        result = SlidingWindowPatterns.longest_substring_without_repeating(s)
        self.assertEqual(result, 1)
        
        # Test case 3: No repeating characters
        s = "pwwkew"
        result = SlidingWindowPatterns.longest_substring_without_repeating(s)
        self.assertEqual(result, 3)  # "wke"
    
    def test_min_window_substring(self):
        """Test minimum window substring."""
        # Test case 1: Normal case
        s = "ADOBECODEBANC"
        t = "ABC"
        result = SlidingWindowPatterns.min_window_substring(s, t)
        self.assertEqual(result, "BANC")
        
        # Test case 2: No valid window
        s = "a"
        t = "aa"
        result = SlidingWindowPatterns.min_window_substring(s, t)
        self.assertEqual(result, "")
        
        # Test case 3: Entire string is minimum window
        s = "a"
        t = "a"
        result = SlidingWindowPatterns.min_window_substring(s, t)
        self.assertEqual(result, "a")
    
    def test_max_consecutive_ones_with_k_flips(self):
        """Test max consecutive ones with k flips."""
        # Test case 1: Normal case
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        result = SlidingWindowPatterns.max_consecutive_ones_with_k_flips(nums, k)
        self.assertEqual(result, 6)
        
        # Test case 2: k = 0
        nums = [1, 1, 0, 1]
        k = 0
        result = SlidingWindowPatterns.max_consecutive_ones_with_k_flips(nums, k)
        self.assertEqual(result, 2)
    
    def test_find_all_anagrams(self):
        """Test finding all anagrams."""
        # Test case 1: Multiple anagrams
        s = "abab"
        p = "ab"
        result = SlidingWindowPatterns.find_all_anagrams(s, p)
        self.assertEqual(result, [0, 2])
        
        # Test case 2: No anagrams
        s = "abcd"
        p = "ef"
        result = SlidingWindowPatterns.find_all_anagrams(s, p)
        self.assertEqual(result, [])


class TestStringManipulationPatterns(unittest.TestCase):
    """Test cases for string manipulation patterns."""
    
    def test_is_anagram(self):
        """Test anagram detection."""
        # Test case 1: Valid anagrams
        self.assertTrue(StringManipulationPatterns.is_anagram("anagram", "nagaram"))
        
        # Test case 2: Not anagrams
        self.assertFalse(StringManipulationPatterns.is_anagram("rat", "car"))
        
        # Test case 3: Different lengths
        self.assertFalse(StringManipulationPatterns.is_anagram("a", "ab"))
    
    def test_group_anagrams(self):
        """Test grouping anagrams."""
        # Test case 1: Multiple groups
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = StringManipulationPatterns.group_anagrams(strs)
        
        # Sort each group and the list of groups for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        self.assertEqual(result_sorted, expected_sorted)
    
    def test_longest_palindromic_substring(self):
        """Test longest palindromic substring."""
        # Test case 1: Odd length palindrome
        s = "babad"
        result = StringManipulationPatterns.longest_palindromic_substring(s)
        self.assertIn(result, ["bab", "aba"])
        
        # Test case 2: Even length palindrome
        s = "cbbd"
        result = StringManipulationPatterns.longest_palindromic_substring(s)
        self.assertEqual(result, "bb")
        
        # Test case 3: Single character
        s = "a"
        result = StringManipulationPatterns.longest_palindromic_substring(s)
        self.assertEqual(result, "a")
    
    def test_string_compression(self):
        """Test string compression."""
        # Test case 1: Compression beneficial
        s = "aabcccccaaa"
        result = StringManipulationPatterns.string_compression(s)
        self.assertEqual(result, "a2b1c5a3")
        
        # Test case 2: Compression not beneficial
        s = "abcdef"
        result = StringManipulationPatterns.string_compression(s)
        self.assertEqual(result, "abcdef")
        
        # Test case 3: Empty string
        s = ""
        result = StringManipulationPatterns.string_compression(s)
        self.assertEqual(result, "")
    
    def test_valid_parentheses(self):
        """Test valid parentheses."""
        # Test case 1: Valid parentheses
        self.assertTrue(StringManipulationPatterns.valid_parentheses("()"))
        self.assertTrue(StringManipulationPatterns.valid_parentheses("()[]{}"))
        self.assertTrue(StringManipulationPatterns.valid_parentheses("{[]}"))
        
        # Test case 2: Invalid parentheses
        self.assertFalse(StringManipulationPatterns.valid_parentheses("(]"))
        self.assertFalse(StringManipulationPatterns.valid_parentheses("([)]"))
        self.assertFalse(StringManipulationPatterns.valid_parentheses("(("))
    
    def test_longest_common_prefix(self):
        """Test longest common prefix."""
        # Test case 1: Common prefix exists
        strs = ["flower", "flow", "flight"]
        result = StringManipulationPatterns.longest_common_prefix(strs)
        self.assertEqual(result, "fl")
        
        # Test case 2: No common prefix
        strs = ["dog", "racecar", "car"]
        result = StringManipulationPatterns.longest_common_prefix(strs)
        self.assertEqual(result, "")
        
        # Test case 3: Single string
        strs = ["hello"]
        result = StringManipulationPatterns.longest_common_prefix(strs)
        self.assertEqual(result, "hello")
    
    def test_reverse_words(self):
        """Test reverse words."""
        # Test case 1: Normal case
        s = "the sky is blue"
        result = StringManipulationPatterns.reverse_words(s)
        self.assertEqual(result, "blue is sky the")
        
        # Test case 2: Extra spaces
        s = "  hello world  "
        result = StringManipulationPatterns.reverse_words(s)
        self.assertEqual(result, "world hello")
        
        # Test case 3: Single word
        s = "hello"
        result = StringManipulationPatterns.reverse_words(s)
        self.assertEqual(result, "hello")
    
    def test_string_to_integer_atoi(self):
        """Test string to integer conversion."""
        # Test case 1: Normal positive number
        self.assertEqual(StringManipulationPatterns.string_to_integer_atoi("42"), 42)
        
        # Test case 2: Negative number with spaces
        self.assertEqual(StringManipulationPatterns.string_to_integer_atoi("   -42"), -42)
        
        # Test case 3: Number with trailing characters
        self.assertEqual(StringManipulationPatterns.string_to_integer_atoi("4193 with words"), 4193)
        
        # Test case 4: Overflow
        self.assertEqual(StringManipulationPatterns.string_to_integer_atoi("91283472332"), 2147483647)
        
        # Test case 5: Invalid input
        self.assertEqual(StringManipulationPatterns.string_to_integer_atoi("words and 987"), 0)
    
    def test_is_subsequence(self):
        """Test subsequence checking."""
        # Test case 1: Valid subsequence
        self.assertTrue(StringManipulationPatterns.is_subsequence("ace", "aec"))
        
        # Test case 2: Not a subsequence
        self.assertFalse(StringManipulationPatterns.is_subsequence("axc", "ahbgdc"))
        
        # Test case 3: Empty subsequence
        self.assertTrue(StringManipulationPatterns.is_subsequence("", "abc"))


class TestAdvancedStringPatterns(unittest.TestCase):
    """Test cases for advanced string patterns."""
    
    def test_kmp_search(self):
        """Test KMP pattern searching."""
        # Test case 1: Pattern found multiple times
        text = "ABABDABACDABABCABCABCABCABC"
        pattern = "ABABCABCABCABC"
        result = AdvancedStringPatterns.kmp_search(text, pattern)
        self.assertEqual(result, [10])
        
        # Test case 2: Pattern not found
        text = "AABAACAADAABAAABAA"
        pattern = "AABA"
        result = AdvancedStringPatterns.kmp_search(text, pattern)
        self.assertEqual(result, [0, 9, 13])
    
    def test_edit_distance(self):
        """Test edit distance calculation."""
        # Test case 1: Normal case
        word1 = "horse"
        word2 = "ros"
        result = AdvancedStringPatterns.edit_distance(word1, word2)
        self.assertEqual(result, 3)
        
        # Test case 2: Same strings
        word1 = "hello"
        word2 = "hello"
        result = AdvancedStringPatterns.edit_distance(word1, word2)
        self.assertEqual(result, 0)
        
        # Test case 3: One empty string
        word1 = "abc"
        word2 = ""
        result = AdvancedStringPatterns.edit_distance(word1, word2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)