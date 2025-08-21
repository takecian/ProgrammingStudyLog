#!/usr/bin/env python3
"""
Comprehensive tests for linked list patterns.
Run with: python test_linked_lists.py
"""

import sys
import traceback

# Import the modules to test
from basic_operations import (
    ListNode, create_linked_list, linked_list_to_list,
    get_length, insert_at_beginning, insert_at_end,
    delete_node_by_value, reverse_linked_list,
    merge_two_sorted_lists, has_cycle, find_middle_node
)
from two_pointers import (
    find_middle_slow_fast, has_cycle_floyd, detect_cycle_start,
    remove_nth_from_end, is_palindrome_two_pointers,
    get_intersection_two_pointers, swap_pairs, add_two_numbers
)
from reversal import (
    reverse_list_iterative, reverse_list_recursive,
    reverse_between, reverse_k_group, is_palindrome_with_reversal
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


def test_basic_operations():
    """Test basic linked list operations."""
    # Test list creation and conversion
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    assert linked_list_to_list(head) == values
    
    # Test length
    assert get_length(head) == 5
    assert get_length(None) == 0
    
    # Test insertion
    head = insert_at_beginning(head, 0)
    assert linked_list_to_list(head) == [0, 1, 2, 3, 4, 5]
    
    head = insert_at_end(head, 6)
    assert linked_list_to_list(head) == [0, 1, 2, 3, 4, 5, 6]
    
    # Test deletion
    head = delete_node_by_value(head, 0)
    assert linked_list_to_list(head) == [1, 2, 3, 4, 5, 6]
    
    head = delete_node_by_value(head, 6)
    assert linked_list_to_list(head) == [1, 2, 3, 4, 5]
    
    # Test reversal
    head = reverse_linked_list(head)
    assert linked_list_to_list(head) == [5, 4, 3, 2, 1]
    
    # Test middle finding
    middle = find_middle_node(head)
    assert middle.val == 3
    
    # Test merge
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = merge_two_sorted_lists(l1, l2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]


def test_two_pointers():
    """Test two-pointer techniques."""
    # Test middle finding
    head = create_linked_list([1, 2, 3, 4, 5])
    middle = find_middle_slow_fast(head)
    assert middle.val == 3
    
    head = create_linked_list([1, 2, 3, 4])
    middle = find_middle_slow_fast(head)
    assert middle.val == 3  # Second middle for even length
    
    # Test cycle detection
    head = create_linked_list([1, 2, 3, 4])
    assert has_cycle_floyd(head) == False
    
    # Create cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
    current = head
    while current.next:
        current = current.next
    cycle_start = head.next  # Node with value 2
    current.next = cycle_start  # Create cycle
    
    assert has_cycle_floyd(head) == True
    detected_start = detect_cycle_start(head)
    assert detected_start == cycle_start
    
    # Test remove nth from end
    head = create_linked_list([1, 2, 3, 4, 5])
    head = remove_nth_from_end(head, 2)
    assert linked_list_to_list(head) == [1, 2, 3, 5]
    
    head = remove_nth_from_end(head, 4)  # Remove first
    assert linked_list_to_list(head) == [2, 3, 5]
    
    # Test palindrome
    palindrome = create_linked_list([1, 2, 2, 1])
    assert is_palindrome_two_pointers(palindrome) == True
    
    not_palindrome = create_linked_list([1, 2, 3, 4])
    assert is_palindrome_two_pointers(not_palindrome) == False
    
    # Test swap pairs
    head = create_linked_list([1, 2, 3, 4])
    head = swap_pairs(head)
    assert linked_list_to_list(head) == [2, 1, 4, 3]
    
    # Test add two numbers
    l1 = create_linked_list([2, 4, 3])  # 342
    l2 = create_linked_list([5, 6, 4])  # 465
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]  # 807


def test_reversal():
    """Test reversal techniques."""
    # Test basic reversal
    head = create_linked_list([1, 2, 3, 4, 5])
    
    # Iterative reversal
    head_iter = reverse_list_iterative(head)
    assert linked_list_to_list(head_iter) == [5, 4, 3, 2, 1]
    
    # Recursive reversal
    head = create_linked_list([1, 2, 3, 4, 5])
    head_rec = reverse_list_recursive(head)
    assert linked_list_to_list(head_rec) == [5, 4, 3, 2, 1]
    
    # Test reverse between positions
    head = create_linked_list([1, 2, 3, 4, 5])
    head = reverse_between(head, 2, 4)  # Reverse positions 2-4
    assert linked_list_to_list(head) == [1, 4, 3, 2, 5]
    
    # Test reverse in k groups
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    head = reverse_k_group(head, 3)
    assert linked_list_to_list(head) == [3, 2, 1, 6, 5, 4]
    
    # Test palindrome with reversal
    palindrome = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome_with_reversal(palindrome) == True
    
    not_palindrome = create_linked_list([1, 2, 3, 4, 5])
    assert is_palindrome_with_reversal(not_palindrome) == False


def test_edge_cases():
    """Test edge cases."""
    # Empty list
    assert linked_list_to_list(None) == []
    assert get_length(None) == 0
    assert reverse_list_iterative(None) is None
    assert has_cycle_floyd(None) == False
    
    # Single node
    single = create_linked_list([1])
    assert linked_list_to_list(single) == [1]
    assert get_length(single) == 1
    assert find_middle_slow_fast(single).val == 1
    assert has_cycle_floyd(single) == False
    
    # Two nodes
    two = create_linked_list([1, 2])
    assert find_middle_slow_fast(two).val == 2
    reversed_two = reverse_list_iterative(two)
    assert linked_list_to_list(reversed_two) == [2, 1]


def test_complex_scenarios():
    """Test complex scenarios."""
    # Large list
    large_values = list(range(1000))
    large_head = create_linked_list(large_values)
    assert get_length(large_head) == 1000
    
    middle = find_middle_slow_fast(large_head)
    assert middle.val == 500  # 0-indexed, so middle is at 500
    
    # Palindrome of various lengths
    odd_palindrome = create_linked_list([1, 2, 3, 2, 1])
    assert is_palindrome_two_pointers(odd_palindrome) == True
    
    even_palindrome = create_linked_list([1, 2, 2, 1])
    assert is_palindrome_two_pointers(even_palindrome) == True
    
    # Remove from various positions
    head = create_linked_list([1, 2, 3, 4, 5])
    head = remove_nth_from_end(head, 1)  # Remove last
    assert linked_list_to_list(head) == [1, 2, 3, 4]
    
    head = remove_nth_from_end(head, 4)  # Remove first
    assert linked_list_to_list(head) == [2, 3, 4]


def main():
    """Run all tests."""
    print("Running Linked List Pattern Tests...")
    print("=" * 50)
    
    tests = [
        ("Basic Operations", test_basic_operations),
        ("Two Pointers", test_two_pointers),
        ("Reversal Patterns", test_reversal),
        ("Edge Cases", test_edge_cases),
        ("Complex Scenarios", test_complex_scenarios),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if run_test(test_name, test_func):
            passed += 1
    
    print("=" * 50)
    print(f"Results: {passed}/{total} test suites passed")
    
    if passed == total:
        print("🎉 All linked list tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())