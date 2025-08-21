"""
Linked List Basic Operations - Fundamental Linked List Patterns

This module contains implementations of basic linked list operations
commonly used in coding interviews.

Common Use Cases:
- Traversal and searching
- Insertion and deletion
- List manipulation and transformation
- Merging and splitting lists
"""

from typing import Optional, List


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """String representation for debugging."""
        return f"ListNode({self.val})"


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Create a linked list from a list of values.
    
    Args:
        values: List of integers to create linked list from
        
    Returns:
        Head of the created linked list
        
    Time: O(n), Space: O(n)
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert linked list to Python list for easy testing.
    
    Args:
        head: Head of linked list
        
    Returns:
        List of values from linked list
        
    Time: O(n), Space: O(n)
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def get_length(head: Optional[ListNode]) -> int:
    """
    Get length of linked list.
    
    Args:
        head: Head of linked list
        
    Returns:
        Length of the linked list
        
    Time: O(n), Space: O(1)
    """
    length = 0
    current = head
    
    while current:
        length += 1
        current = current.next
    
    return length


def get_nth_node(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Get the nth node (0-indexed) from the linked list.
    
    Args:
        head: Head of linked list
        n: Index of node to retrieve (0-indexed)
        
    Returns:
        The nth node, or None if index is out of bounds
        
    Time: O(n), Space: O(1)
    """
    current = head
    index = 0
    
    while current and index < n:
        current = current.next
        index += 1
    
    return current


def insert_at_beginning(head: Optional[ListNode], val: int) -> ListNode:
    """
    Insert a new node at the beginning of the list.
    
    Args:
        head: Current head of linked list
        val: Value to insert
        
    Returns:
        New head of the linked list
        
    Time: O(1), Space: O(1)
    """
    new_node = ListNode(val)
    new_node.next = head
    return new_node


def insert_at_end(head: Optional[ListNode], val: int) -> ListNode:
    """
    Insert a new node at the end of the list.
    
    Args:
        head: Head of linked list
        val: Value to insert
        
    Returns:
        Head of the linked list
        
    Time: O(n), Space: O(1)
    """
    new_node = ListNode(val)
    
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head


def insert_at_position(head: Optional[ListNode], val: int, pos: int) -> ListNode:
    """
    Insert a new node at the specified position (0-indexed).
    
    Args:
        head: Head of linked list
        val: Value to insert
        pos: Position to insert at (0-indexed)
        
    Returns:
        Head of the linked list
        
    Time: O(n), Space: O(1)
    """
    if pos == 0:
        return insert_at_beginning(head, val)
    
    new_node = ListNode(val)
    current = head
    
    # Navigate to position - 1
    for _ in range(pos - 1):
        if not current:
            return head  # Position out of bounds
        current = current.next
    
    if current:
        new_node.next = current.next
        current.next = new_node
    
    return head


def delete_node_by_value(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    Delete the first node with the specified value.
    
    Args:
        head: Head of linked list
        val: Value to delete
        
    Returns:
        Head of the modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    # If head needs to be deleted
    if head.val == val:
        return head.next
    
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            return head
        current = current.next
    
    return head


def delete_node_at_position(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    """
    Delete node at specified position (0-indexed).
    
    Args:
        head: Head of linked list
        pos: Position to delete (0-indexed)
        
    Returns:
        Head of the modified linked list
        
    Time: O(n), Space: O(1)
    """
    if not head or pos < 0:
        return head
    
    # Delete head
    if pos == 0:
        return head.next
    
    current = head
    for _ in range(pos - 1):
        if not current or not current.next:
            return head  # Position out of bounds
        current = current.next
    
    if current.next:
        current.next = current.next.next
    
    return head


def search_value(head: Optional[ListNode], val: int) -> bool:
    """
    Search for a value in the linked list.
    
    Args:
        head: Head of linked list
        val: Value to search for
        
    Returns:
        True if value is found, False otherwise
        
    Time: O(n), Space: O(1)
    """
    current = head
    
    while current:
        if current.val == val:
            return True
        current = current.next
    
    return False


def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node of the linked list.
    For even length, returns the second middle node.
    
    Args:
        head: Head of linked list
        
    Returns:
        Middle node of the list
        
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list iteratively.
    
    Args:
        head: Head of linked list to reverse
        
    Returns:
        Head of the reversed linked list
        
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev


def reverse_linked_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list recursively.
    
    Args:
        head: Head of linked list to reverse
        
    Returns:
        Head of the reversed linked list
        
    Time: O(n), Space: O(n) due to recursion stack
    """
    # Base case
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest
    new_head = reverse_linked_list_recursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head


def merge_two_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        l1: Head of first sorted linked list
        l2: Head of second sorted linked list
        
    Returns:
        Head of merged sorted linked list
        
    Time: O(m + n), Space: O(1)
    """
    # Create dummy node to simplify logic
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 or l2
    
    return dummy.next


def remove_duplicates_sorted(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicates from a sorted linked list.
    
    Args:
        head: Head of sorted linked list
        
    Returns:
        Head of list with duplicates removed
        
    Time: O(n), Space: O(1)
    """
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if linked list has a cycle using Floyd's algorithm.
    
    Args:
        head: Head of linked list
        
    Returns:
        True if cycle exists, False otherwise
        
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def get_intersection_node(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the intersection node of two linked lists.
    
    Args:
        headA: Head of first linked list
        headB: Head of second linked list
        
    Returns:
        Intersection node, or None if no intersection
        
    Time: O(m + n), Space: O(1)
    """
    if not headA or not headB:
        return None
    
    # Get lengths
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    # Align starting positions
    currA, currB = headA, headB
    
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next
    
    # Find intersection
    while currA and currB:
        if currA == currB:
            return currA
        currA = currA.next
        currB = currB.next
    
    return None


# Interview Tips and Common Patterns
"""
Linked List Interview Tips:

1. **Key Techniques**:
   - Two pointers (slow/fast) for cycle detection and middle finding
   - Dummy nodes to simplify edge cases
   - Recursive vs iterative approaches
   - In-place manipulation to save space

2. **Common Patterns**:
   - Traversal with pointer manipulation
   - Reversal (iterative and recursive)
   - Merging sorted lists
   - Cycle detection (Floyd's algorithm)
   - Finding intersections

3. **Edge Cases to Consider**:
   - Empty list (head is None)
   - Single node list
   - Lists of different lengths
   - Cycles in the list
   - Null pointer handling

4. **Python-Specific Tips**:
   - Use dummy nodes to avoid special cases
   - Leverage tuple unpacking: a, b = b, a
   - Use 'or' operator for default values: current.next = l1 or l2
   - Remember that None is falsy in boolean context

5. **Time/Space Complexity**:
   - Most operations are O(n) time
   - In-place operations are O(1) space
   - Recursive solutions use O(n) space for call stack
   - Hash tables can reduce time complexity but increase space

6. **Common Mistakes**:
   - Not handling None pointers
   - Losing reference to nodes during manipulation
   - Off-by-one errors in position-based operations
   - Not updating head pointer when needed
   - Memory leaks in languages with manual memory management
"""