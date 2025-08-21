"""
Linked List Reversal Patterns - List Reversal Techniques

This module contains implementations of various linked list reversal patterns
commonly encountered in coding interviews.

Common Use Cases:
- Reverse entire linked list
- Reverse linked list in groups
- Reverse between specific positions
- Palindrome checking with reversal
- Reordering lists using reversal
"""

from typing import Optional
from basic_operations import ListNode, create_linked_list, linked_list_to_list


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list iteratively.
    
    Args:
        head: Head of linked list to reverse
        
    Returns:
        Head of reversed linked list
        
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current           # Move prev forward
        current = next_temp      # Move current forward
    
    return prev  # prev is now the new head


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list recursively.
    
    Args:
        head: Head of linked list to reverse
        
    Returns:
        Head of reversed linked list
        
    Time: O(n), Space: O(n) due to recursion stack
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    Reverse linked list from position left to right (1-indexed).
    
    Args:
        head: Head of linked list
        left: Starting position (1-indexed)
        right: Ending position (1-indexed)
        
    Returns:
        Head of modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head or left == right:
        return head
    
    # Create dummy node to handle edge case where left = 1
    dummy = ListNode(0)
    dummy.next = head
    
    # Find the node before the reversal starts
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    
    # Start of reversal
    current = prev.next
    
    # Reverse the sublist
    for _ in range(right - left):
        next_temp = current.next
        current.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp
    
    return dummy.next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Reverse nodes in k-group. If remaining nodes < k, leave as is.
    
    Args:
        head: Head of linked list
        k: Group size for reversal
        
    Returns:
        Head of modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head or k == 1:
        return head
    
    # Check if we have at least k nodes
    def has_k_nodes(node, k):
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        return count == k
    
    if not has_k_nodes(head, k):
        return head
    
    # Reverse first k nodes
    prev = None
    current = head
    
    for _ in range(k):
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    # Recursively reverse remaining groups
    if current:
        head.next = reverse_k_group(current, k)
    
    return prev  # New head of current group


def reverse_alternate_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Reverse alternate k-groups in linked list.
    
    Args:
        head: Head of linked list
        k: Group size for reversal
        
    Returns:
        Head of modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head or k == 1:
        return head
    
    def reverse_k_nodes(node, k):
        """Reverse k nodes starting from node."""
        prev = None
        current = node
        
        for _ in range(k):
            if not current:
                break
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev, current  # new_head, next_node
    
    def skip_k_nodes(node, k):
        """Skip k nodes and return the next node."""
        for _ in range(k):
            if not node:
                break
            node = node.next
        return node
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    
    while True:
        # Check if we have k nodes to reverse
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next
        
        group_next = kth_node.next
        
        # Reverse current group
        group_start = prev_group_end.next
        new_head, _ = reverse_k_nodes(group_start, k)
        
        # Connect with previous part
        prev_group_end.next = new_head
        group_start.next = group_next
        prev_group_end = group_start
        
        # Skip next k nodes (don't reverse)
        for _ in range(k):
            if not prev_group_end.next:
                return dummy.next
            prev_group_end = prev_group_end.next
    
    return dummy.next


def swap_pairs_reversal(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swap every two adjacent nodes using reversal concept.
    
    Args:
        head: Head of linked list
        
    Returns:
        Head of modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        # Identify the two nodes to be swapped
        first = prev.next
        second = prev.next.next
        
        # Swapping (reverse the pair)
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move prev to end of swapped pair
        prev = first
    
    return dummy.next


def reverse_print(head: Optional[ListNode]) -> None:
    """
    Print linked list in reverse order without modifying it.
    
    Args:
        head: Head of linked list
        
    Time: O(n), Space: O(n) due to recursion
    """
    if not head:
        return
    
    # Recursively go to end
    reverse_print(head.next)
    
    # Print on way back
    print(head.val, end=" ")


def is_palindrome_with_reversal(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome by reversing second half.
    
    Args:
        head: Head of linked list
        
    Returns:
        True if palindrome, False otherwise
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return True
    
    # Find middle using slow/fast pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = reverse_list_iterative(slow)
    
    # Compare first and second halves
    first_half = head
    result = True
    
    while second_half:  # second_half might be shorter
        if first_half.val != second_half.val:
            result = False
            break
        first_half = first_half.next
        second_half = second_half.next
    
    # Optional: restore original list
    # reverse_list_iterative(second_half_head)
    
    return result


def add_two_numbers_reverse(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Add two numbers where digits are stored in forward order.
    
    Args:
        l1: First number (most significant digit first)
        l2: Second number (most significant digit first)
        
    Returns:
        Sum as linked list (most significant digit first)
        
    Time: O(max(m, n)), Space: O(max(m, n))
    """
    # Reverse both lists to make addition easier
    l1_rev = reverse_list_iterative(l1)
    l2_rev = reverse_list_iterative(l2)
    
    # Add reversed numbers
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1_rev or l2_rev or carry:
        val1 = l1_rev.val if l1_rev else 0
        val2 = l2_rev.val if l2_rev else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        l1_rev = l1_rev.next if l1_rev else None
        l2_rev = l2_rev.next if l2_rev else None
    
    # Reverse result to get correct order
    return reverse_list_iterative(dummy.next)


def reverse_nodes_in_even_length_groups(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse nodes in even-length groups.
    Groups are: [1], [2,3], [4,5,6], [7,8,9,10], ...
    
    Args:
        head: Head of linked list
        
    Returns:
        Head of modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    group_size = 1
    
    while prev.next:
        # Find the end of current group
        group_start = prev.next
        group_end = group_start
        count = 1
        
        # Move to end of group or end of list
        while group_end.next and count < group_size:
            group_end = group_end.next
            count += 1
        
        next_group_start = group_end.next
        
        # Reverse if group has even length
        if count % 2 == 0:
            # Reverse the group
            group_end.next = None  # Temporarily cut the list
            new_group_start = reverse_list_iterative(group_start)
            
            # Reconnect
            prev.next = new_group_start
            group_start.next = next_group_start
            prev = group_start
        else:
            # Don't reverse, just move prev
            prev = group_end
        
        group_size += 1
    
    return dummy.next


# Helper function for testing
def print_list(head: Optional[ListNode]) -> None:
    """Print linked list for debugging."""
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


# Interview Tips and Common Patterns
"""
Linked List Reversal - Interview Tips:

1. **Basic Reversal Pattern**:
   ```python
   prev = None
   current = head
   while current:
       next_temp = current.next
       current.next = prev
       prev = current
       current = next_temp
   return prev
   ```

2. **Key Techniques**:
   - Iterative reversal: O(1) space, easier to understand
   - Recursive reversal: O(n) space, more elegant
   - Partial reversal: reverse between positions
   - Group reversal: reverse in chunks of k

3. **Common Patterns**:
   - Use dummy nodes for edge cases
   - Store next node before breaking links
   - Update pointers in correct order
   - Handle remaining nodes after group operations

4. **Edge Cases**:
   - Empty list or single node
   - Reversing entire list vs partial
   - Groups that don't divide evenly
   - Position-based operations (1-indexed vs 0-indexed)

5. **Python-Specific Tips**:
   - Use tuple unpacking: prev, current.next = current, prev
   - Leverage truthiness of None
   - Use dummy nodes to simplify logic
   - Remember to return correct head

6. **Applications**:
   - Palindrome checking
   - Number addition (forward/reverse order)
   - Reordering lists
   - Implementing stacks with linked lists

7. **Time/Space Complexity**:
   - Iterative: O(n) time, O(1) space
   - Recursive: O(n) time, O(n) space
   - Group operations: O(n) time, O(1) space
   - Most efficient approach depends on constraints

8. **Common Mistakes**:
   - Losing reference to next node
   - Not updating head pointer
   - Off-by-one errors in position calculations
   - Not handling edge cases properly
   - Forgetting to reconnect after partial reversal
"""