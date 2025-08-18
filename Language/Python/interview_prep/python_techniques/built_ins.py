"""
Essential built-in function examples and usage patterns for coding interviews.

This module provides comprehensive examples of Python built-in functions that are
commonly useful in coding interviews, with practical usage patterns and explanations.
"""

from typing import List, Tuple, Any, Iterator
import itertools


class BuiltInTechniques:
    """Collection of essential built-in function patterns for interviews."""
    
    @staticmethod
    def enumerate_patterns() -> dict:
        """Examples of enumerate() usage in interview problems."""
        return {
            "basic_indexing": """
# Get both index and value while iterating
nums = [10, 20, 30, 40]
for i, val in enumerate(nums):
    print(f"Index {i}: {val}")
""",
            
            "find_target_indices": """
# Find all indices where condition is met
def find_indices(nums, target):
    return [i for i, val in enumerate(nums) if val == target]
""",
            
            "two_sum_pattern": """
# Classic two-sum using enumerate
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
""",
            
            "start_parameter": """
# Using start parameter for custom indexing
words = ['apple', 'banana', 'cherry']
for i, word in enumerate(words, start=1):
    print(f"{i}. {word}")  # 1-indexed output
"""
        }
    
    @staticmethod
    def zip_patterns() -> dict:
        """Examples of zip() usage for parallel iteration."""
        return {
            "parallel_iteration": """
# Iterate over multiple lists simultaneously
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
""",
            
            "matrix_operations": """
# Transpose matrix using zip
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
""",
            
            "merge_sorted_arrays": """
# Merge two sorted arrays element by element
def merge_arrays(arr1, arr2):
    return [a + b for a, b in zip(arr1, arr2)]
""",
            
            "coordinate_pairs": """
# Create coordinate pairs from x and y lists
x_coords = [1, 2, 3, 4]
y_coords = [5, 6, 7, 8]
points = list(zip(x_coords, y_coords))  # [(1, 5), (2, 6), (3, 7), (4, 8)]
"""
        }
    
    @staticmethod
    def map_patterns() -> dict:
        """Examples of map() for functional transformations."""
        return {
            "type_conversion": """
# Convert string input to integers
input_line = "1 2 3 4 5"
numbers = list(map(int, input_line.split()))
""",
            
            "apply_function": """
# Apply function to all elements
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared = list(map(square, nums))  # [1, 4, 9, 16, 25]
""",
            
            "lambda_transformation": """
# Use with lambda for simple transformations
strings = ['hello', 'world', 'python']
lengths = list(map(lambda s: len(s), strings))  # [5, 5, 6]
""",
            
            "multiple_iterables": """
# Map over multiple iterables
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(add, list1, list2))  # [5, 7, 9]
"""
        }
    
    @staticmethod
    def filter_patterns() -> dict:
        """Examples of filter() for conditional selection."""
        return {
            "basic_filtering": """
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
""",
            
            "filter_with_function": """
# Filter using custom function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(2, 20)
primes = list(filter(is_prime, numbers))
""",
            
            "filter_strings": """
# Filter strings by length
words = ['cat', 'elephant', 'dog', 'hippopotamus', 'ant']
long_words = list(filter(lambda w: len(w) > 5, words))
""",
            
            "filter_none_values": """
# Remove None values from list
mixed_list = [1, None, 2, None, 3, 4, None]
clean_list = list(filter(None, mixed_list))  # [1, 2, 3, 4]
"""
        }
    
    @staticmethod
    def any_all_patterns() -> dict:
        """Examples of any() and all() for boolean operations."""
        return {
            "any_examples": """
# Check if any element satisfies condition
numbers = [1, 3, 5, 7, 8]
has_even = any(x % 2 == 0 for x in numbers)  # True (8 is even)

# Check if any string starts with vowel
words = ['hello', 'world', 'apple']
starts_with_vowel = any(word[0].lower() in 'aeiou' for word in words)
""",
            
            "all_examples": """
# Check if all elements satisfy condition
numbers = [2, 4, 6, 8, 10]
all_even = all(x % 2 == 0 for x in numbers)  # True

# Check if all strings are uppercase
words = ['HELLO', 'WORLD', 'PYTHON']
all_upper = all(word.isupper() for word in words)
""",
            
            "validation_patterns": """
# Validate input data
def validate_positive_numbers(nums):
    return all(x > 0 for x in nums)

def has_duplicates(nums):
    return any(nums.count(x) > 1 for x in nums)
""",
            
            "matrix_validation": """
# Check matrix properties
def is_square_matrix(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def has_zero_row(matrix):
    return any(all(cell == 0 for cell in row) for row in matrix)
"""
        }
    
    @staticmethod
    def sorted_patterns() -> dict:
        """Examples of sorted() with custom key functions."""
        return {
            "basic_sorting": """
# Sort with custom key
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
by_grade = sorted(students, key=lambda x: x[1])  # Sort by grade
by_name = sorted(students, key=lambda x: x[0])   # Sort by name
""",
            
            "reverse_sorting": """
# Sort in descending order
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
desc_sorted = sorted(numbers, reverse=True)
""",
            
            "complex_sorting": """
# Sort by multiple criteria
points = [(1, 3), (2, 1), (1, 1), (2, 3)]
# Sort by x-coordinate, then by y-coordinate (descending)
sorted_points = sorted(points, key=lambda p: (p[0], -p[1]))
""",
            
            "string_sorting": """
# Sort strings by length, then alphabetically
words = ['python', 'java', 'c', 'javascript', 'go']
sorted_words = sorted(words, key=lambda w: (len(w), w))
""",
            
            "custom_objects": """
# Sort custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
by_age = sorted(people, key=lambda p: p.age)
"""
        }
    
    @staticmethod
    def range_patterns() -> dict:
        """Examples of range() for iteration and sequence generation."""
        return {
            "basic_ranges": """
# Different range patterns
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)
""",
            
            "reverse_iteration": """
# Iterate in reverse
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)

# Reverse index iteration
arr = [1, 2, 3, 4, 5]
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])  # 5, 4, 3, 2, 1
""",
            
            "matrix_iteration": """
# Iterate over matrix indices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
""",
            
            "sliding_window": """
# Generate sliding window indices
def sliding_window_indices(arr, window_size):
    for i in range(len(arr) - window_size + 1):
        yield (i, i + window_size)

arr = [1, 2, 3, 4, 5, 6]
for start, end in sliding_window_indices(arr, 3):
    print(arr[start:end])  # [1,2,3], [2,3,4], [3,4,5], [4,5,6]
"""
        }
    
    @staticmethod
    def min_max_patterns() -> dict:
        """Examples of min() and max() with key functions."""
        return {
            "basic_min_max": """
# Find min/max with custom criteria
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
best_student = max(students, key=lambda x: x[1])    # ('Bob', 90)
worst_student = min(students, key=lambda x: x[1])   # ('Charlie', 78)
""",
            
            "string_operations": """
# Find longest/shortest string
words = ['python', 'java', 'c', 'javascript']
longest = max(words, key=len)   # 'javascript'
shortest = min(words, key=len)  # 'c'
""",
            
            "coordinate_operations": """
# Find closest/farthest point from origin
points = [(1, 2), (3, 4), (0, 1), (5, 0)]
closest = min(points, key=lambda p: p[0]**2 + p[1]**2)
farthest = max(points, key=lambda p: p[0]**2 + p[1]**2)
""",
            
            "default_values": """
# Use default parameter to handle empty sequences
empty_list = []
safe_min = min(empty_list, default=0)  # Returns 0 instead of error
safe_max = max(empty_list, default=float('-inf'))
"""
        }
    
    @staticmethod
    def sum_patterns() -> dict:
        """Examples of sum() for aggregation operations."""
        return {
            "basic_sum": """
# Sum with different start values
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)           # 15
total_plus_10 = sum(numbers, 10)  # 25
""",
            
            "conditional_sum": """
# Sum with conditions using generator expressions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(x for x in numbers if x % 2 == 0)  # 30
square_sum = sum(x**2 for x in numbers)           # 385
""",
            
            "nested_sum": """
# Sum elements in nested structures
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = sum(sum(row) for row in matrix)  # 45

# Alternative using itertools.chain
from itertools import chain
total_alt = sum(chain.from_iterable(matrix))
""",
            
            "weighted_sum": """
# Calculate weighted sum
values = [10, 20, 30]
weights = [0.5, 0.3, 0.2]
weighted_sum = sum(v * w for v, w in zip(values, weights))
"""
        }


def demonstrate_built_ins():
    """Demonstrate all built-in function patterns."""
    techniques = BuiltInTechniques()
    
    print("=== ENUMERATE PATTERNS ===")
    for name, code in techniques.enumerate_patterns().items():
        print(f"\n{name.upper()}:")
        print(code.strip())
    
    print("\n=== ZIP PATTERNS ===")
    for name, code in techniques.zip_patterns().items():
        print(f"\n{name.upper()}:")
        print(code.strip())
    
    print("\n=== MAP PATTERNS ===")
    for name, code in techniques.map_patterns().items():
        print(f"\n{name.upper()}:")
        print(code.strip())


if __name__ == "__main__":
    demonstrate_built_ins()