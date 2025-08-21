"""
Binary Search Tree Patterns - BST Operations and Properties

This module contains implementations of BST operations and validation
commonly encountered in coding interviews.

BST Property: For every node, left subtree values < node value < right subtree values

Common Use Cases:
- BST validation and construction
- Search, insertion, and deletion
- Finding kth smallest/largest elements
- Range queries and closest values
- BST to sorted array conversion
"""

from typing import Optional, List, Tuple
from tree_traversal import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Validate if binary tree is a valid BST.
    
    Args:
        root: Root of binary tree
        
    Returns:
        True if valid BST, False otherwise
        
    Time: O(n), Space: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """
    Validate BST using inorder traversal property.
    
    Args:
        root: Root of binary tree
        
    Returns:
        True if valid BST, False otherwise
        
    Time: O(n), Space: O(h)
    """
    def inorder(node):
        if not node:
            return True
        
        if not inorder(node.left):
            return False
        
        if node.val <= inorder.prev:
            return False
        inorder.prev = node.val
        
        return inorder(node.right)
    
    inorder.prev = float('-inf')
    return inorder(root)


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Search for a value in BST.
    
    Args:
        root: Root of BST
        val: Value to search for
        
    Returns:
        Node containing the value, or None if not found
        
    Time: O(h), Space: O(1) iterative, O(h) recursive
    """
    current = root
    
    while current:
        if val == current.val:
            return current
        elif val < current.val:
            current = current.left
        else:
            current = current.right
    
    return None


def search_bst_recursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Search for a value in BST recursively.
    
    Args:
        root: Root of BST
        val: Value to search for
        
    Returns:
        Node containing the value, or None if not found
        
    Time: O(h), Space: O(h)
    """
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst_recursive(root.left, val)
    else:
        return search_bst_recursive(root.right, val)


def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Insert a value into BST.
    
    Args:
        root: Root of BST
        val: Value to insert
        
    Returns:
        Root of modified BST
        
    Time: O(h), Space: O(1) iterative, O(h) recursive
    """
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root


def insert_into_bst_iterative(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Insert a value into BST iteratively.
    
    Args:
        root: Root of BST
        val: Value to insert
        
    Returns:
        Root of modified BST
        
    Time: O(h), Space: O(1)
    """
    if not root:
        return TreeNode(val)
    
    current = root
    while True:
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = TreeNode(val)
                break
            current = current.right
    
    return root


def delete_node_bst(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    Delete a node from BST.
    
    Args:
        root: Root of BST
        key: Value to delete
        
    Returns:
        Root of modified BST
        
    Time: O(h), Space: O(h)
    """
    if not root:
        return None
    
    if key < root.val:
        root.left = delete_node_bst(root.left, key)
    elif key > root.val:
        root.right = delete_node_bst(root.right, key)
    else:
        # Node to delete found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # Node has two children - find inorder successor
            successor = find_min(root.right)
            root.val = successor.val
            root.right = delete_node_bst(root.right, successor.val)
    
    return root


def find_min(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Find minimum value node in BST.
    
    Args:
        root: Root of BST
        
    Returns:
        Node with minimum value
        
    Time: O(h), Space: O(1)
    """
    if not root:
        return None
    
    while root.left:
        root = root.left
    
    return root


def find_max(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Find maximum value node in BST.
    
    Args:
        root: Root of BST
        
    Returns:
        Node with maximum value
        
    Time: O(h), Space: O(1)
    """
    if not root:
        return None
    
    while root.right:
        root = root.right
    
    return root


def kth_smallest_bst(root: Optional[TreeNode], k: int) -> int:
    """
    Find kth smallest element in BST.
    
    Args:
        root: Root of BST
        k: Position (1-indexed)
        
    Returns:
        Value of kth smallest element
        
    Time: O(h + k), Space: O(h)
    """
    def inorder(node):
        if not node:
            return None
        
        # Search left subtree
        left_result = inorder(node.left)
        if left_result is not None:
            return left_result
        
        # Process current node
        inorder.count += 1
        if inorder.count == k:
            return node.val
        
        # Search right subtree
        return inorder(node.right)
    
    inorder.count = 0
    return inorder(root)


def kth_largest_bst(root: Optional[TreeNode], k: int) -> int:
    """
    Find kth largest element in BST.
    
    Args:
        root: Root of BST
        k: Position (1-indexed)
        
    Returns:
        Value of kth largest element
        
    Time: O(h + k), Space: O(h)
    """
    def reverse_inorder(node):
        if not node:
            return None
        
        # Search right subtree first (largest values)
        right_result = reverse_inorder(node.right)
        if right_result is not None:
            return right_result
        
        # Process current node
        reverse_inorder.count += 1
        if reverse_inorder.count == k:
            return node.val
        
        # Search left subtree
        return reverse_inorder(node.left)
    
    reverse_inorder.count = 0
    return reverse_inorder(root)


def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find lowest common ancestor in BST.
    
    Args:
        root: Root of BST
        p: First node
        q: Second node
        
    Returns:
        LCA node
        
    Time: O(h), Space: O(1) iterative, O(h) recursive
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    
    return None


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    Calculate sum of values in BST within given range.
    
    Args:
        root: Root of BST
        low: Lower bound (inclusive)
        high: Upper bound (inclusive)
        
    Returns:
        Sum of values in range [low, high]
        
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    total = 0
    
    # Add current node if in range
    if low <= root.val <= high:
        total += root.val
    
    # Recursively search left and right subtrees
    if root.val > low:
        total += range_sum_bst(root.left, low, high)
    if root.val < high:
        total += range_sum_bst(root.right, low, high)
    
    return total


def closest_value_bst(root: Optional[TreeNode], target: float) -> int:
    """
    Find value in BST closest to target.
    
    Args:
        root: Root of BST
        target: Target value
        
    Returns:
        Value closest to target
        
    Time: O(h), Space: O(1)
    """
    closest = root.val
    
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        
        if target < root.val:
            root = root.left
        else:
            root = root.right
    
    return closest


def closest_k_values_bst(root: Optional[TreeNode], target: float, k: int) -> List[int]:
    """
    Find k values in BST closest to target.
    
    Args:
        root: Root of BST
        target: Target value
        k: Number of closest values to find
        
    Returns:
        List of k closest values
        
    Time: O(n), Space: O(n)
    """
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        
        if len(result) < k:
            result.append(node.val)
        else:
            # Check if current value is closer than the farthest in result
            if abs(node.val - target) < abs(result[0] - target):
                result.pop(0)  # Remove farthest
                result.append(node.val)
        
        inorder(node.right)
    
    result = []
    inorder(root)
    return sorted(result, key=lambda x: abs(x - target))


def convert_bst_to_greater_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Convert BST to Greater Sum Tree (each node = sum of all greater nodes).
    
    Args:
        root: Root of BST
        
    Returns:
        Root of modified tree
        
    Time: O(n), Space: O(h)
    """
    def reverse_inorder(node):
        if not node:
            return
        
        reverse_inorder(node.right)  # Process larger values first
        
        reverse_inorder.sum += node.val
        node.val = reverse_inorder.sum
        
        reverse_inorder(node.left)
    
    reverse_inorder.sum = 0
    reverse_inorder(root)
    return root


def bst_to_sorted_array(root: Optional[TreeNode]) -> List[int]:
    """
    Convert BST to sorted array using inorder traversal.
    
    Args:
        root: Root of BST
        
    Returns:
        Sorted array of values
        
    Time: O(n), Space: O(n)
    """
    result = []
    
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    """
    Convert sorted array to height-balanced BST.
    
    Args:
        nums: Sorted array of integers
        
    Returns:
        Root of balanced BST
        
    Time: O(n), Space: O(log n)
    """
    def build_tree(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        root.left = build_tree(left, mid - 1)
        root.right = build_tree(mid + 1, right)
        
        return root
    
    return build_tree(0, len(nums) - 1)


def trim_bst(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    """
    Trim BST to contain only values in range [low, high].
    
    Args:
        root: Root of BST
        low: Lower bound
        high: Upper bound
        
    Returns:
        Root of trimmed BST
        
    Time: O(n), Space: O(h)
    """
    if not root:
        return None
    
    if root.val < low:
        return trim_bst(root.right, low, high)
    elif root.val > high:
        return trim_bst(root.left, low, high)
    else:
        root.left = trim_bst(root.left, low, high)
        root.right = trim_bst(root.right, low, high)
        return root


# Interview Tips and Common Patterns
"""
Binary Search Tree Interview Tips:

1. **BST Properties**:
   - Left subtree values < root < right subtree values
   - Inorder traversal gives sorted sequence
   - Search, insert, delete in O(h) time
   - Height h ranges from log n (balanced) to n (skewed)

2. **Common Patterns**:
   - Validation: Use min/max bounds or inorder traversal
   - Search: Compare with current node, go left or right
   - Insertion: Find correct position, create new node
   - Deletion: Handle 3 cases (0, 1, or 2 children)

3. **Key Insights**:
   - Inorder traversal of BST is sorted
   - Use BST property to prune search space
   - LCA in BST: first node where paths diverge
   - Range queries: prune subtrees outside range

4. **Optimization Techniques**:
   - Early termination in range queries
   - Iterative solutions to save space
   - Use BST property to avoid full traversal
   - Balance tree for better performance

5. **Python-Specific Tips**:
   - Use float('-inf') and float('inf') for bounds
   - Leverage truthiness of None
   - Use nonlocal for nested function counters
   - Consider using deque for level-order operations

6. **Common Mistakes**:
   - Not handling duplicate values correctly
   - Forgetting to update parent pointers in deletion
   - Not considering empty tree cases
   - Confusing BST validation with simple comparison

7. **Time/Space Complexity**:
   - Search/Insert/Delete: O(h) time, O(1) space iterative
   - Traversal operations: O(n) time, O(h) space
   - Construction from sorted array: O(n) time, O(log n) space
   - Validation: O(n) time, O(h) space

8. **Applications**:
   - Maintaining sorted data with dynamic updates
   - Range queries and closest value searches
   - Expression trees and decision trees
   - Database indexing and file systems
"""