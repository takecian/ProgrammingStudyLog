# Python Techniques for Coding Interviews

This module provides comprehensive Python techniques, algorithms, and utilities specifically designed for coding interviews. It covers essential built-in functions, data structures from the collections module, common algorithms, and utility functions for input/output handling.

## Modules Overview

### 1. `built_ins.py` - Essential Built-in Functions
Contains examples and patterns for Python's most useful built-in functions:
- `enumerate()` - Index and value iteration
- `zip()` - Parallel iteration
- `map()` - Functional transformations
- `filter()` - Conditional selection
- `any()`/`all()` - Boolean operations
- `sorted()` - Custom sorting
- `range()` - Sequence generation
- `min()`/`max()` - Finding extremes
- `sum()` - Aggregation operations

### 2. `data_structures.py` - Collections Module Techniques
Covers essential data structures from Python's collections module:
- `defaultdict` - Automatic default values
- `Counter` - Frequency counting
- `deque` - Double-ended queue
- `heapq` - Priority queue operations
- Advanced patterns combining multiple data structures

### 3. `algorithms.py` - Common Algorithm Implementations
Pythonic implementations of fundamental algorithms:
- **Search Algorithms**: Binary search variants, peak finding
- **Sorting Algorithms**: Quick sort, merge sort, heap sort, counting sort
- **Graph Algorithms**: DFS, BFS, shortest path, cycle detection, topological sort
- **Dynamic Programming**: Fibonacci, LIS, LCS, knapsack, coin change
- **String Algorithms**: KMP search, longest palindromic substring

### 4. `interview_utils.py` - Input/Output and Testing Utilities
Utility functions for interview problem solving:
- **Input Parsing**: Reading integers, matrices, graphs, test cases
- **Output Formatting**: Printing results in various formats
- **Testing Utils**: Function timing, test case running, debugging
- **Data Structure Helpers**: Building graphs, prefix sums
- **String Helpers**: Palindrome checking, anagram detection
- **Math Helpers**: GCD, LCM, prime checking, modular arithmetic

## Usage Examples

### Built-in Functions
```python
from python_techniques.built_ins import BuiltInTechniques

# Get examples of enumerate patterns
patterns = BuiltInTechniques.enumerate_patterns()
print(patterns['two_sum_pattern'])

# Two-sum implementation using enumerate
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Collections Module
```python
from python_techniques.data_structures import CollectionsTechniques
from collections import defaultdict, Counter, deque

# Build graph adjacency list
def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# Count character frequencies
def char_frequency(s):
    return Counter(s)

# BFS using deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result
```

### Algorithms
```python
from python_techniques.algorithms import SearchAlgorithms, GraphAlgorithms

# Binary search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = SearchAlgorithms.binary_search(arr, 5)

# Graph traversal
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
dfs_result = GraphAlgorithms.dfs_iterative(graph, 'A')
bfs_result = GraphAlgorithms.bfs(graph, 'A')
```

### Input/Output Utilities
```python
from python_techniques.interview_utils import InputParser, OutputFormatter

# Read input (in actual interview, this would read from stdin)
# n = InputParser.read_int()
# matrix = InputParser.read_matrix(n)

# Format output
result = [1, 2, 3, 4, 5]
OutputFormatter.print_list(result)  # "1 2 3 4 5"
OutputFormatter.print_yes_no(True)  # "YES"
```

### Testing and Debugging
```python
from python_techniques.interview_utils import TestingUtils

def add(a, b):
    return a + b

# Create and run test cases
test_cases = [
    TestingUtils.generate_test_case(add, [2, 3], 5),
    TestingUtils.generate_test_case(add, [0, 0], 0),
    TestingUtils.generate_test_case(add, [-1, 1], 0)
]

passed, total = TestingUtils.run_test_cases(test_cases)
print(f"Passed {passed}/{total} tests")
```

## Key Features

1. **Interview-Focused**: All examples and patterns are specifically chosen for their relevance to coding interviews
2. **Pythonic**: Emphasizes Python idioms and built-in optimizations
3. **Comprehensive**: Covers the most common algorithm and data structure patterns
4. **Practical**: Includes real-world examples and complete implementations
5. **Well-Documented**: Each function includes clear explanations and usage examples

## Integration with Existing Repository

This module integrates seamlessly with the existing competitive programming solutions:
- References existing algorithm implementations in `Libs/`
- Extends `snippet_for_leetcode.py` patterns
- Provides interview-specific versions of competitive programming techniques
- Cross-references with existing LeetCode solutions

## Best Practices for Interviews

1. **Start Simple**: Begin with brute force solutions, then optimize
2. **Use Built-ins**: Leverage Python's powerful built-in functions
3. **Think in Patterns**: Recognize common problem patterns and apply appropriate techniques
4. **Test Thoroughly**: Use the testing utilities to verify your solutions
5. **Communicate Clearly**: Practice explaining your approach and complexity analysis

This module serves as a comprehensive reference for Python coding interviews, providing both the technical knowledge and practical tools needed for success.