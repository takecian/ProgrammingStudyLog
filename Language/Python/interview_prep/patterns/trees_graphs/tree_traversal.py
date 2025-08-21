"""
Tree Traversal Patterns - DFS/BFS Implementations and Variations

This module contains implementations of various tree traversal algorithms
commonly used in coding interviews.

Common Use Cases:
- Tree traversal (preorder, inorder, postorder)
- Level-order traversal (BFS)
- Tree construction from traversals
- Path finding and tree analysis
- Tree modification and validation
"""

from typing import List, Optional, Deque
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


def create_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Create binary tree from level-order list representation.
    None represents missing nodes.
    
    Args:
        values: Level-order representation of tree
        
    Returns:
        Root of created tree
        
    Time: O(n), Space: O(n)
    """
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# DFS Traversals - Recursive
def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder traversal: Root -> Left -> Right
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in preorder
        
    Time: O(n), Space: O(h) where h is height
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)  # Visit root
        dfs(node.left)           # Traverse left
        dfs(node.right)          # Traverse right
    
    dfs(root)
    return result


def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder traversal: Left -> Root -> Right
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in inorder
        
    Time: O(n), Space: O(h)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # Traverse left
        result.append(node.val)  # Visit root
        dfs(node.right)          # Traverse right
    
    dfs(root)
    return result


def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder traversal: Left -> Right -> Root
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in postorder
        
    Time: O(n), Space: O(h)
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # Traverse left
        dfs(node.right)          # Traverse right
        result.append(node.val)  # Visit root
    
    dfs(root)
    return result


# DFS Traversals - Iterative
def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder traversal using stack.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in preorder
        
    Time: O(n), Space: O(h)
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first, then left (stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder traversal using stack.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in inorder
        
    Time: O(n), Space: O(h)
    """
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder traversal using two stacks.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in postorder
        
    Time: O(n), Space: O(h)
    """
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    
    # First stack for traversal, second for result order
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        # Push left first, then right
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Pop from second stack for postorder
    result = []
    while stack2:
        result.append(stack2.pop().val)
    
    return result


# BFS Traversal
def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level-order traversal (BFS) returning levels separately.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of lists, each containing values at that level
        
    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_values)
    
    return result


def level_order_flat(root: Optional[TreeNode]) -> List[int]:
    """
    Level-order traversal returning flat list.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of values in level order
        
    Time: O(n), Space: O(w)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Zigzag level-order traversal (alternating left-right, right-left).
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of lists with zigzag order
        
    Time: O(n), Space: O(w)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse for right-to-left levels
        if not left_to_right:
            level_values.reverse()
        
        result.append(level_values)
        left_to_right = not left_to_right
    
    return result


def vertical_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Vertical order traversal (nodes at same column).
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of lists, each containing values in same column
        
    Time: O(n log n), Space: O(n)
    """
    if not root:
        return []
    
    # Map column -> list of (row, value) pairs
    column_map = {}
    queue = deque([(root, 0, 0)])  # (node, row, col)
    
    while queue:
        node, row, col = queue.popleft()
        
        if col not in column_map:
            column_map[col] = []
        column_map[col].append((row, node.val))
        
        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))
    
    # Sort columns and within each column by row, then by value
    result = []
    for col in sorted(column_map.keys()):
        column_map[col].sort()  # Sort by row, then by value
        result.append([val for row, val in column_map[col]])
    
    return result


# Tree Analysis Functions
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Maximum depth
        
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Minimum depth to a leaf
        
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    
    # If one subtree is empty, return depth of other + 1
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    
    # Both subtrees exist
    return 1 + min(min_depth(root.left), min_depth(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Check if binary tree is height-balanced.
    
    Args:
        root: Root of binary tree
        
    Returns:
        True if balanced, False otherwise
        
    Time: O(n), Space: O(h)
    """
    def check_balance(node):
        if not node:
            return 0, True  # height, is_balanced
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        height = 1 + max(left_height, right_height)
        balanced = (left_balanced and right_balanced and 
                   abs(left_height - right_height) <= 1)
        
        return height, balanced
    
    _, balanced = check_balance(root)
    return balanced


def diameter_of_tree(root: Optional[TreeNode]) -> int:
    """
    Find diameter of binary tree (longest path between any two nodes).
    
    Args:
        root: Root of binary tree
        
    Returns:
        Diameter of tree
        
    Time: O(n), Space: O(h)
    """
    max_diameter = 0
    
    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        
        # Diameter through current node
        current_diameter = left_depth + right_depth
        max_diameter = max(max_diameter, current_diameter)
        
        # Return depth of current subtree
        return 1 + max(left_depth, right_depth)
    
    dfs(root)
    return max_diameter


def all_paths_to_leaves(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Find all root-to-leaf paths.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of paths, each path is a list of values
        
    Time: O(n * h), Space: O(n * h)
    """
    if not root:
        return []
    
    paths = []
    
    def dfs(node, current_path):
        if not node:
            return
        
        current_path.append(node.val)
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            paths.append(current_path[:])  # Copy the path
        else:
            dfs(node.left, current_path)
            dfs(node.right, current_path)
        
        current_path.pop()  # Backtrack
    
    dfs(root, [])
    return paths


# Interview Tips and Common Patterns
"""
Tree Traversal Interview Tips:

1. **Traversal Types**:
   - Preorder: Root -> Left -> Right (good for copying tree)
   - Inorder: Left -> Root -> Right (gives sorted order for BST)
   - Postorder: Left -> Right -> Root (good for deletion)
   - Level-order: BFS, level by level

2. **Recursive vs Iterative**:
   - Recursive: Cleaner code, O(h) space for call stack
   - Iterative: More control, explicit stack management
   - BFS: Always iterative with queue

3. **Common Patterns**:
   - DFS for path problems and tree analysis
   - BFS for level-based problems and shortest paths
   - Two-pointer techniques for tree problems
   - Divide and conquer for tree construction

4. **Key Insights**:
   - Inorder of BST gives sorted sequence
   - Preorder + Inorder can reconstruct tree
   - Postorder good for bottom-up processing
   - Level-order good for level-based analysis

5. **Python-Specific Tips**:
   - Use collections.deque for BFS queue
   - Leverage list slicing for path copying
   - Use nonlocal for nested function variables
   - Consider using defaultdict for grouping

6. **Edge Cases**:
   - Empty tree (root is None)
   - Single node tree
   - Skewed trees (essentially linked lists)
   - Perfect binary trees

7. **Time/Space Complexity**:
   - All traversals: O(n) time
   - Recursive: O(h) space for call stack
   - Iterative: O(h) space for explicit stack
   - BFS: O(w) space where w is maximum width

8. **Common Applications**:
   - Tree validation (BST, balanced, etc.)
   - Path finding and sum problems
   - Tree construction and serialization
   - Level-based processing
   - Tree comparison and analysis
"""