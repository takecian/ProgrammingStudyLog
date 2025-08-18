"""
Collections module techniques for coding interviews.

This module provides comprehensive examples of Python's collections module
data structures that are essential for efficient interview problem solving.
"""

from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from typing import List, Dict, Any, Optional, Tuple
import heapq


class CollectionsTechniques:
    """Collection of collections module patterns for interviews."""
    
    @staticmethod
    def defaultdict_patterns() -> dict:
        """Examples of defaultdict usage in interview problems."""
        return {
            "graph_adjacency_list": """
# Build adjacency list for graph problems
from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    return graph

edges = [(1, 2), (2, 3), (3, 4), (1, 4)]
graph = build_graph(edges)
""",
            
            "group_by_key": """
# Group items by a key
def group_words_by_length(words):
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)

words = ['cat', 'dog', 'elephant', 'ant', 'python']
grouped = group_words_by_length(words)
# {3: ['cat', 'dog', 'ant'], 8: ['elephant'], 6: ['python']}
""",
            
            "nested_defaultdict": """
# Create nested defaultdict for 2D structures
def create_2d_defaultdict():
    return defaultdict(lambda: defaultdict(int))

# Usage for counting pairs
pair_counts = create_2d_defaultdict()
pairs = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b')]
for x, y in pairs:
    pair_counts[x][y] += 1
""",
            
            "anagram_grouping": """
# Group anagrams using defaultdict
def group_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)
    return list(anagram_groups.values())

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
groups = group_anagrams(words)
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""
        }
    
    @staticmethod
    def counter_patterns() -> dict:
        """Examples of Counter usage for frequency counting."""
        return {
            "frequency_counting": """
# Count character frequencies
from collections import Counter

def char_frequency(s):
    return Counter(s)

text = "hello world"
freq = char_frequency(text)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
""",
            
            "most_common": """
# Find most common elements
def find_most_common(items, n=3):
    counter = Counter(items)
    return counter.most_common(n)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
top_3 = find_most_common(numbers, 3)
# [(4, 4), (3, 3), (2, 2)]
""",
            
            "counter_arithmetic": """
# Counter arithmetic operations
from collections import Counter

counter1 = Counter(['a', 'b', 'c', 'a'])
counter2 = Counter(['a', 'b', 'b', 'd'])

# Addition
combined = counter1 + counter2
# Counter({'a': 3, 'b': 3, 'c': 1, 'd': 1})

# Subtraction
difference = counter1 - counter2
# Counter({'c': 1, 'a': 1})

# Intersection (minimum counts)
intersection = counter1 & counter2
# Counter({'a': 1, 'b': 1})
""",
            
            "valid_anagram": """
# Check if two strings are anagrams
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

# Alternative: check if one is subset of another
def can_form_word(letters, word):
    return not (Counter(word) - Counter(letters))
""",
            
            "missing_elements": """
# Find missing elements using Counter
def find_missing_numbers(nums, target_range):
    num_counter = Counter(nums)
    target_counter = Counter(range(target_range[0], target_range[1] + 1))
    missing = target_counter - num_counter
    return list(missing.elements())
"""
        }
    
    @staticmethod
    def deque_patterns() -> dict:
        """Examples of deque usage for efficient queue/stack operations."""
        return {
            "bfs_queue": """
# BFS traversal using deque
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] 
                        if neighbor not in visited)
    return result
""",
            
            "sliding_window_maximum": """
# Sliding window maximum using deque
def sliding_window_maximum(nums, k):
    dq = deque()  # Store indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
""",
            
            "palindrome_checker": """
# Check palindrome using deque
def is_palindrome(s):
    dq = deque(char.lower() for char in s if char.isalnum())
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
""",
            
            "recent_counter": """
# Implement recent counter with deque
class RecentCounter:
    def __init__(self):
        self.requests = deque()
    
    def ping(self, t):
        self.requests.append(t)
        # Remove requests older than 3000ms
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
""",
            
            "rotate_operations": """
# Efficient rotation using deque
def rotate_array(arr, k):
    dq = deque(arr)
    dq.rotate(k)  # Rotate right by k positions
    return list(dq)

# Manual rotation
def rotate_left(arr, k):
    dq = deque(arr)
    for _ in range(k):
        dq.append(dq.popleft())
    return list(dq)
"""
        }
    
    @staticmethod
    def heapq_patterns() -> dict:
        """Examples of heapq usage for priority queue operations."""
        return {
            "basic_heap_operations": """
# Basic heap operations
import heapq

# Min heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)

smallest = heapq.heappop(heap)  # 1

# Convert list to heap
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)  # In-place heapification
""",
            
            "k_largest_elements": """
# Find k largest elements
def k_largest(nums, k):
    return heapq.nlargest(k, nums)

def k_smallest(nums, k):
    return heapq.nsmallest(k, nums)

# For custom objects
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
top_students = heapq.nlargest(2, students, key=lambda x: x[1])
""",
            
            "merge_k_sorted_lists": """
# Merge k sorted lists using heap
def merge_k_sorted_lists(lists):
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result
""",
            
            "max_heap_simulation": """
# Simulate max heap using negative values
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, -val)
    
    def pop(self):
        return -heapq.heappop(self.heap)
    
    def peek(self):
        return -self.heap[0] if self.heap else None
""",
            
            "median_finder": """
# Find median using two heaps
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap
    
    def add_number(self, num):
        heapq.heappush(self.small, -num)
        
        # Balance heaps
        if (self.small and self.large and 
            -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Ensure size difference <= 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
"""
        }
    
    @staticmethod
    def advanced_patterns() -> dict:
        """Advanced patterns combining multiple collections."""
        return {
            "lru_cache_implementation": """
# LRU Cache using OrderedDict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)
""",
            
            "word_pattern_matching": """
# Word pattern matching using multiple data structures
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True
""",
            
            "top_k_frequent": """
# Top K frequent elements using Counter and heap
def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Alternative using bucket sort
def top_k_frequent_bucket(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        buckets[freq].append(num)
    
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            break
    
    return result[:k]
""",
            
            "design_twitter": """
# Design Twitter using multiple data structures
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(deque)  # userId -> tweets
        self.following = defaultdict(set)  # userId -> set of followees
        self.timestamp = 0
    
    def post_tweet(self, userId, tweetId):
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1
        # Keep only recent 10 tweets
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
    
    def get_news_feed(self, userId):
        # Get tweets from user and followees
        all_tweets = []
        
        # Add user's tweets
        all_tweets.extend(self.tweets[userId])
        
        # Add followees' tweets
        for followeeId in self.following[userId]:
            all_tweets.extend(self.tweets[followeeId])
        
        # Sort by timestamp and return top 10
        all_tweets.sort(reverse=True)
        return [tweetId for _, tweetId in all_tweets[:10]]
    
    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
"""
        }


class DataStructureUtils:
    """Utility functions for common data structure operations."""
    
    @staticmethod
    def create_frequency_map(items: List[Any]) -> Dict[Any, int]:
        """Create frequency map using Counter."""
        return dict(Counter(items))
    
    @staticmethod
    def create_graph_from_edges(edges: List[Tuple[Any, Any]], directed: bool = False) -> Dict[Any, List[Any]]:
        """Create adjacency list representation of graph."""
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
        return dict(graph)
    
    @staticmethod
    def group_by_key(items: List[Any], key_func) -> Dict[Any, List[Any]]:
        """Group items by a key function."""
        groups = defaultdict(list)
        for item in items:
            key = key_func(item)
            groups[key].append(item)
        return dict(groups)
    
    @staticmethod
    def sliding_window_deque(arr: List[Any], window_size: int):
        """Generate sliding windows using deque."""
        if window_size > len(arr):
            return
        
        window = deque()
        for i in range(window_size):
            window.append(arr[i])
        yield list(window)
        
        for i in range(window_size, len(arr)):
            window.popleft()
            window.append(arr[i])
            yield list(window)


def demonstrate_collections():
    """Demonstrate collections module patterns."""
    techniques = CollectionsTechniques()
    
    print("=== DEFAULTDICT PATTERNS ===")
    for name, code in techniques.defaultdict_patterns().items():
        print(f"\n{name.upper()}:")
        print(code.strip())
    
    print("\n=== COUNTER PATTERNS ===")
    for name, code in techniques.counter_patterns().items():
        print(f"\n{name.upper()}:")
        print(code.strip())


if __name__ == "__main__":
    demonstrate_collections()