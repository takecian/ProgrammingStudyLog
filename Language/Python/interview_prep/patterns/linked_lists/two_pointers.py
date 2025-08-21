"""
Linked List Two Pointers - Fast/Slow Pointer Techniques

This module contains implementations of two-pointer techniques specifically
for linked lists, including fast/slow pointers and other pointer manipulation patterns.

Common Use Cases:
- Cycle detection (Floyd's algorithm)
- Finding middle of linked list
- Removing nth node from end
- Palindrome checking
- Finding intersection points
"""

from typing import Optional
from basic_operations import ListNode, create_linked_list, linked_list_to_list


def find_middle_slow_fast(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node using slow/fast pointers.
    For even length, returns the second middle node.
    
    Args:
        head: Head of linked list
        
    Returns:
        Middle node
        
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def find_middle_first_of_two(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node, returning first middle for even length lists.
    
    Args:
        head: Head of linked list
        
    Returns:
        First middle node for even length, middle for odd length
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return head
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def has_cycle_floyd(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using Floyd's Cycle Detection Algorithm.
    
    Args:
        head: Head of linked list
        
    Returns:
        True if cycle exists, False otherwise
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    # Phase 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the starting node of the cycle in a linked list.
    
    Args:
        head: Head of linked list
        
    Returns:
        Starting node of cycle, or None if no cycle
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    # Phase 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle found
    
    # Phase 2: Find cycle start
    # Move one pointer to head, keep other at meeting point
    # Move both one step at a time until they meet
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from the end of linked list.
    
    Args:
        head: Head of linked list
        n: Position from end to remove (1-indexed)
        
    Returns:
        Head of modified linked list
        
    Time: O(L) where L is length, Space: O(1)
    """
    # Use dummy node to handle edge case of removing head
    dummy = ListNode(0)
    dummy.next = head
    
    # Set up two pointers with n+1 gap
    first = second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from end
    second.next = second.next.next
    
    return dummy.next


def is_palindrome_two_pointers(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is a palindrome using two pointers.
    
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
    def reverse_list(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second_half = reverse_list(slow)
    
    # Compare first and second halves
    first_half = head
    while second_half:  # second_half might be shorter for odd length
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True


def get_intersection_two_pointers(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find intersection of two linked lists using two pointers.
    
    Args:
        headA: Head of first linked list
        headB: Head of second linked list
        
    Returns:
        Intersection node, or None if no intersection
        
    Time: O(m + n), Space: O(1)
    """
    if not headA or not headB:
        return None
    
    ptrA, ptrB = headA, headB
    
    # When one pointer reaches end, redirect to other list's head
    # This ensures both pointers travel same distance
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    
    return ptrA  # Either intersection node or None


def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorder list: L0 → L1 → … → Ln-1 → Ln becomes L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
    
    Args:
        head: Head of linked list to reorder
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return
    
    # Step 1: Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second_half = reverse_list(slow.next)
    slow.next = None  # Cut the list
    
    # Step 3: Merge two halves alternately
    first_half = head
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        
        first_half.next = second_half
        second_half.next = temp1
        
        first_half = temp1
        second_half = temp2


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swap every two adjacent nodes in linked list.
    
    Args:
        head: Head of linked list
        
    Returns:
        Head of modified linked list
        
    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        # Nodes to be swapped
        first = prev.next
        second = prev.next.next
        
        # Swapping
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move prev pointer
        prev = first
    
    return dummy.next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Rotate linked list to the right by k places.
    
    Args:
        head: Head of linked list
        k: Number of places to rotate right
        
    Returns:
        Head of rotated linked list
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next or k == 0:
        return head
    
    # Find length and make it circular
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    tail.next = head  # Make circular
    
    # Find new tail (length - k % length - 1 steps from head)
    k = k % length
    steps_to_new_tail = length - k
    
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None  # Break the circle
    
    return new_head


def partition_list(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    Partition linked list around value x, preserving original relative order.
    
    Args:
        head: Head of linked list
        x: Partition value
        
    Returns:
        Head of partitioned linked list
        
    Time: O(n), Space: O(1)
    """
    # Create two dummy nodes for before and after lists
    before_head = ListNode(0)
    after_head = ListNode(0)
    
    before = before_head
    after = after_head
    
    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next
    
    # Connect the two lists
    after.next = None  # Important: terminate the after list
    before.next = after_head.next
    
    return before_head.next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Add two numbers represented as linked lists (digits in reverse order).
    
    Args:
        l1: First number as linked list
        l2: Second number as linked list
        
    Returns:
        Sum as linked list
        
    Time: O(max(m, n)), Space: O(max(m, n))
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


# Template for two-pointer linked list problems
def two_pointer_template(head: Optional[ListNode], gap: int = 1):
    """
    Generic template for two-pointer linked list problems.
    
    Args:
        head: Head of linked list
        gap: Initial gap between pointers
        
    Returns:
        Depends on specific problem
    """
    if not head:
        return None
    
    slow = fast = head
    
    # Create initial gap
    for _ in range(gap):
        if not fast:
            return None
        fast = fast.next
    
    # Move both pointers until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# Interview Tips and Common Patterns
"""
Two Pointers in Linked Lists - Interview Tips:

1. **Fast/Slow Pointer (Floyd's Algorithm)**:
   - Cycle detection: fast moves 2 steps, slow moves 1
   - Finding middle: when fast reaches end, slow is at middle
   - Finding cycle start: reset one pointer to head after detection

2. **Gap-Based Two Pointers**:
   - Remove nth from end: maintain gap of n+1
   - Find kth from end: maintain gap of k

3. **Common Patterns**:
   - Use dummy nodes to simplify edge cases
   - Break and reconnect links carefully
   - Consider odd/even length differences
   - Handle null pointers gracefully

4. **Key Insights**:
   - Two pointers can solve many problems in O(1) space
   - Fast/slow pattern works for cycle detection and middle finding
   - Gap-based pattern works for position-relative problems
   - Always consider edge cases: empty list, single node, etc.

5. **Python-Specific Tips**:
   - Use tuple unpacking for swaps: a, b = b, a
   - Leverage truthiness: while fast and fast.next
   - Use dummy nodes to avoid special head cases
   - Remember to handle None gracefully

6. **Common Mistakes**:
   - Not handling null pointers
   - Off-by-one errors in gap calculations
   - Forgetting to break cycles when creating them
   - Not considering edge cases (empty, single node)
   - Losing references to nodes during manipulation

7. **Time/Space Complexity**:
   - Most two-pointer solutions are O(n) time, O(1) space
   - This is often better than hash table solutions (O(n) space)
   - Recursive solutions use O(n) space for call stack
"""