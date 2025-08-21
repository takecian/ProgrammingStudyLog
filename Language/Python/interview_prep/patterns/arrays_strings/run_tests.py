#!/usr/bin/env python3
"""
Simple test runner for array and string patterns.
Run with: python run_tests.py
"""

import sys
import traceback

# Import the modules to test
from two_pointers import (
    two_sum_sorted, is_palindrome, remove_duplicates, 
    container_with_most_water, three_sum, sort_colors
)
from sliding_window import (
    max_sum_subarray_size_k, longest_substring_without_repeating,
    longest_substring_k_distinct, min_window_substring,
    subarray_sum_equals_k, max_consecutive_ones_k_flips,
    character_replacement, find_all_anagrams
)
from string_manipulation import (
    reverse_string, reverse_words, is_anagram, group_anagrams,
    longest_common_prefix, valid_palindrome, string_to_integer,
    zigzag_conversion, longest_palindromic_substring,
    encode_decode_strings, decode_strings, multiply_strings,
    word_pattern, simplify_path
)


def run_test(test_name, test_func):
    """Run a single test and report results."""
    try:
        test_func()
        print(f"✓ {test_name}")
        return True
    except Exception as e:
        print(f"✗ {test_name}: {str(e)}")
        traceback.print_exc()
        return False


def test_two_pointers():
    """Test two-pointer functions."""
    # Test two_sum_sorted
    assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_sorted([1, 2, 3, 4], 10) is None
    
    # Test is_palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    
    # Test remove_duplicates
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2
    assert nums[:2] == [1, 2]
    
    # Test container_with_most_water
    assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test three_sum
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2
    
    # Test sort_colors
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_sliding_window():
    """Test sliding window functions."""
    # Test max_sum_subarray_size_k
    assert max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3) == 9
    
    # Test longest_substring_without_repeating
    assert longest_substring_without_repeating("abcabcbb") == 3
    assert longest_substring_without_repeating("bbbbb") == 1
    
    # Test longest_substring_k_distinct
    assert longest_substring_k_distinct("eceba", 2) == 3
    
    # Test min_window_substring
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    
    # Test subarray_sum_equals_k
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    
    # Test max_consecutive_ones_k_flips
    assert max_consecutive_ones_k_flips([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    
    # Test character_replacement
    assert character_replacement("ABAB", 2) == 4
    
    # Test find_all_anagrams
    assert find_all_anagrams("abab", "ab") == [0, 2]


def test_string_manipulation():
    """Test string manipulation functions."""
    # Test reverse_string
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]
    
    # Test reverse_words
    assert reverse_words("the sky is blue") == "blue is sky the"
    
    # Test is_anagram
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    
    # Test group_anagrams
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(result) == 3
    
    # Test longest_common_prefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    
    # Test valid_palindrome
    assert valid_palindrome("A man, a plan, a canal: Panama") == True
    
    # Test string_to_integer
    assert string_to_integer("42") == 42
    assert string_to_integer("   -42") == -42
    
    # Test zigzag_conversion
    assert zigzag_conversion("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    
    # Test longest_palindromic_substring
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]
    
    # Test encode/decode strings
    strs = ["lint", "code", "love", "you"]
    encoded = encode_decode_strings(strs)
    decoded = decode_strings(encoded)
    assert decoded == strs
    
    # Test multiply_strings
    assert multiply_strings("2", "3") == "6"
    assert multiply_strings("123", "456") == "56088"
    
    # Test word_pattern
    assert word_pattern("abba", "dog cat cat dog") == True
    assert word_pattern("abba", "dog cat cat fish") == False
    
    # Test simplify_path
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/../") == "/"


def main():
    """Run all tests."""
    print("Running Array and String Pattern Tests...")
    print("=" * 50)
    
    tests = [
        ("Two Pointers", test_two_pointers),
        ("Sliding Window", test_sliding_window),
        ("String Manipulation", test_string_manipulation),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if run_test(test_name, test_func):
            passed += 1
    
    print("=" * 50)
    print(f"Results: {passed}/{total} test suites passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())