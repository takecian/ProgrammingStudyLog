"""
Pythonic implementations of common algorithms for coding interviews.

This module provides clean, efficient Python implementations of fundamental
algorithms commonly encountered in coding interviews, emphasizing Python
idioms and built-in optimizations.
"""

from typing import List, Optional, Tuple, Dict, Any
from collections import deque, defaultdict
import heapq
import bisect


class SearchAlgorithms:
    """Pythonic implementations of search algorithms."""
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """
        Binary search implementation.
        Returns index of target, or -1 if not found.
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def binary_search_leftmost(arr: List[int], target: int) -> int:
        """Find leftmost occurrence of target."""
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left if left < len(arr) and arr[left] == target else -1
    
    @staticmethod
    def binary_search_rightmost(arr: List[int], target: int) -> int:
        """Find rightmost occurrence of target."""
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left - 1 if left > 0 and arr[left - 1] == target else -1
    
    @staticmethod
    def search_range(arr: List[int], target: int) -> List[int]:
        """Find first and last position of target in sorted array."""
        left = SearchAlgorithms.binary_search_leftmost(arr, target)
        if left == -1:
            return [-1, -1]
        right = SearchAlgorithms.binary_search_rightmost(arr, target)
        return [left, right]
    
    @staticmethod
    def search_insert_position(arr: List[int], target: int) -> int:
        """Find position where target should be inserted."""
        return bisect.bisect_left(arr, target)
    
    @staticmethod
    def find_peak_element(arr: List[int]) -> int:
        """Find any peak element in array."""
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left


class SortingAlgorithms:
    """Pythonic implementations of sorting algorithms."""
    
    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        """Quick sort implementation."""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return (SortingAlgorithms.quick_sort(left) + 
                middle + 
                SortingAlgorithms.quick_sort(right))
    
    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """Merge sort implementation."""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays."""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def heap_sort(arr: List[int]) -> List[int]:
        """Heap sort using heapq."""
        heap = arr.copy()
        heapq.heapify(heap)
        return [heapq.heappop(heap) for _ in range(len(heap))]
    
    @staticmethod
    def counting_sort(arr: List[int]) -> List[int]:
        """Counting sort for integers."""
        if not arr:
            return arr
        
        min_val, max_val = min(arr), max(arr)
        range_size = max_val - min_val + 1
        count = [0] * range_size
        
        # Count occurrences
        for num in arr:
            count[num - min_val] += 1
        
        # Reconstruct sorted array
        result = []
        for i, freq in enumerate(count):
            result.extend([i + min_val] * freq)
        
        return result
    
    @staticmethod
    def bucket_sort(arr: List[float], num_buckets: int = 10) -> List[float]:
        """Bucket sort for floating point numbers."""
        if not arr:
            return arr
        
        # Create buckets
        buckets = [[] for _ in range(num_buckets)]
        
        # Distribute elements into buckets
        min_val, max_val = min(arr), max(arr)
        range_size = max_val - min_val
        
        for num in arr:
            if range_size == 0:
                bucket_index = 0
            else:
                bucket_index = min(int((num - min_val) / range_size * num_buckets), 
                                 num_buckets - 1)
            buckets[bucket_index].append(num)
        
        # Sort individual buckets and concatenate
        result = []
        for bucket in buckets:
            result.extend(sorted(bucket))
        
        return result


class GraphAlgorithms:
    """Pythonic implementations of graph algorithms."""
    
    @staticmethod
    def dfs_recursive(graph: Dict[Any, List[Any]], start: Any, visited: set = None) -> List[Any]:
        """Depth-first search (recursive)."""
        if visited is None:
            visited = set()
        
        result = []
        if start not in visited:
            visited.add(start)
            result.append(start)
            
            for neighbor in graph.get(start, []):
                result.extend(GraphAlgorithms.dfs_recursive(graph, neighbor, visited))
        
        return result
    
    @staticmethod
    def dfs_iterative(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
        """Depth-first search (iterative)."""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Add neighbors in reverse order to maintain left-to-right traversal
                stack.extend(reversed(graph.get(node, [])))
        
        return result
    
    @staticmethod
    def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
        """Breadth-first search."""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(neighbor for neighbor in graph.get(node, []) 
                           if neighbor not in visited)
        
        return result
    
    @staticmethod
    def shortest_path_bfs(graph: Dict[Any, List[Any]], start: Any, end: Any) -> Optional[List[Any]]:
        """Find shortest path using BFS."""
        if start == end:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])
        
        while queue:
            node, path = queue.popleft()
            if node not in visited:
                visited.add(node)
                
                for neighbor in graph.get(node, []):
                    if neighbor == end:
                        return path + [neighbor]
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return None
    
    @staticmethod
    def has_cycle_directed(graph: Dict[Any, List[Any]]) -> bool:
        """Detect cycle in directed graph using DFS."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        
        def dfs(node):
            if color[node] == GRAY:
                return True  # Back edge found
            if color[node] == BLACK:
                return False
            
            color[node] = GRAY
            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True
            color[node] = BLACK
            return False
        
        for node in graph:
            if color[node] == WHITE:
                if dfs(node):
                    return True
        return False
    
    @staticmethod
    def topological_sort(graph: Dict[Any, List[Any]]) -> Optional[List[Any]]:
        """Topological sort using DFS."""
        if GraphAlgorithms.has_cycle_directed(graph):
            return None
        
        visited = set()
        stack = []
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
        
        for node in graph:
            if node not in visited:
                dfs(node)
        
        return stack[::-1]
    
    @staticmethod
    def dijkstra(graph: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Dict[Any, int]:
        """Dijkstra's shortest path algorithm."""
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0
        heap = [(0, start)]
        visited = set()
        
        while heap:
            current_dist, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, weight in graph.get(node, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        
        return dict(distances)


class DynamicProgramming:
    """Common dynamic programming patterns."""
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """Fibonacci with memoization."""
        memo = {}
        
        def fib(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
        
        return fib(n)
    
    @staticmethod
    def fibonacci_iterative(n: int) -> int:
        """Space-optimized iterative fibonacci."""
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def longest_increasing_subsequence(arr: List[int]) -> int:
        """Length of longest increasing subsequence."""
        if not arr:
            return 0
        
        # dp[i] = length of LIS ending at index i
        dp = [1] * len(arr)
        
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    @staticmethod
    def longest_common_subsequence(text1: str, text2: str) -> int:
        """Length of longest common subsequence."""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
        """0/1 Knapsack problem."""
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                # Don't take item i-1
                dp[i][w] = dp[i - 1][w]
                
                # Take item i-1 if possible
                if weights[i - 1] <= w:
                    dp[i][w] = max(dp[i][w], 
                                 dp[i - 1][w - weights[i - 1]] + values[i - 1])
        
        return dp[n][capacity]
    
    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        """Minimum coins needed to make amount."""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


class StringAlgorithms:
    """String processing algorithms."""
    
    @staticmethod
    def kmp_search(text: str, pattern: str) -> List[int]:
        """KMP string matching algorithm."""
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        if not pattern:
            return []
        
        lps = compute_lps(pattern)
        matches = []
        i = j = 0
        
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return matches
    
    @staticmethod
    def longest_palindromic_substring(s: str) -> str:
        """Find longest palindromic substring."""
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Odd length palindromes
            len1 = expand_around_center(i, i)
            # Even length palindromes
            len2 = expand_around_center(i, i + 1)
            
            current_max = max(len1, len2)
            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2
        
        return s[start:start + max_len]


def demonstrate_algorithms():
    """Demonstrate algorithm implementations."""
    # Test search algorithms
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Binary search for 5: {SearchAlgorithms.binary_search(arr, 5)}")
    
    # Test sorting algorithms
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"Quick sort: {SortingAlgorithms.quick_sort(unsorted)}")
    
    # Test graph algorithms
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(f"DFS from A: {GraphAlgorithms.dfs_iterative(graph, 'A')}")
    print(f"BFS from A: {GraphAlgorithms.bfs(graph, 'A')}")


if __name__ == "__main__":
    demonstrate_algorithms()