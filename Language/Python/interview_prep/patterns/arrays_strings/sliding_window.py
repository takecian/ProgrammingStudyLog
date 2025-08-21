"""
Sliding Window Pattern for Arrays and Strings

The sliding window technique is used to solve problems involving subarrays or substrings
by maintaining a window that slides through the data structure. This pattern is particularly
effective for problems involving contiguous sequences.

Time Complexity: Usually O(n)
Space Complexity: Usually O(1) to O(k) where k is window size

Common use cases:
- Maximum/minimum subarray of size k
- Maximum/minimum subarray problems
- Substring problems with constraints
- Finding patterns in strings
- Fixed or variable window size problems
- Longest substring with k distinct characters
- Minimum window substring
- Subarray sum equals k
- Longest substring without repeating characters
"""

from typing import List, Dict, Optional
from collections import defaultdict, Counter


<<<<<<< HEAD
class SlidingWindowPatterns:
    """Collection of sliding window pattern implementations and templates."""
    
    @staticmethod
    def max_sum_subarray_fixed_size(nums: List[int], k: int) -> int:
        """
        Find maximum sum of subarray with fixed size k.
        
        Time: O(n), Space: O(1)
        
        Template for: Fixed window size problems
        """
        if len(nums) < k:
            return 0
        
        # Calculate sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            # Remove leftmost element, add rightmost element
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum
    
    @staticmethod
    def longest_substring_without_repeating(s: str) -> int:
        """
        Find length of longest substring without repeating characters.
        
        Time: O(n), Space: O(min(m,n)) where m is charset size
        
        Template for: Variable window with uniqueness constraint
        """
        char_index = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If character seen before and within current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    @staticmethod
    def min_window_substring(s: str, t: str) -> str:
        """
        Find minimum window substring containing all characters of t.
        
        Time: O(|s| + |t|), Space: O(|s| + |t|)
        
        Template for: Minimum window with character frequency constraints
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Sliding window variables
        left = right = 0
        formed = 0  # Number of unique chars in window with desired frequency
        
        # Dictionary to keep count of characters in current window
        window_counts = defaultdict(int)
        
        # Result: (window length, left, right)
        ans = float('inf'), None, None
        
        while right < len(s):
            # Add character from right to window
            char = s[right]
            window_counts[char] += 1
            
            # Check if frequency matches desired count in t
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Try to contract window from left
            while left <= right and formed == required:
                char = s[left]
                
                # Update result if this window is smaller
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove leftmost character
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
    
    @staticmethod
    def longest_subarray_with_sum_k(nums: List[int], k: int) -> int:
        """
        Find longest subarray with sum equal to k (for positive numbers).
        
        Time: O(n), Space: O(1)
        
        Template for: Variable window with sum constraint
        """
        left = 0
        current_sum = 0
        max_length = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window while sum is greater than k
            while current_sum > k and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # Check if we found target sum
            if current_sum == k:
                max_length = max(max_length, right - left + 1)
        
        return max_length
    
    @staticmethod
    def max_consecutive_ones_with_k_flips(nums: List[int], k: int) -> int:
        """
        Find max consecutive 1s after flipping at most k zeros.
        
        Time: O(n), Space: O(1)
        
        Template for: Variable window with constraint on operations
        """
        left = 0
        zeros_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Expand window
            if nums[right] == 0:
                zeros_count += 1
            
            # Shrink window if constraint violated
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        """
        Find longest substring with same character after k replacements.
        
        Time: O(n), Space: O(1) - at most 26 characters
        
        Template for: Variable window with replacement constraint
        """
        char_count = defaultdict(int)
        left = 0
        max_length = 0
        max_char_count = 0
        
        for right in range(len(s)):
            # Expand window
            char_count[s[right]] += 1
            max_char_count = max(max_char_count, char_count[s[right]])
            
            # Current window size
            window_size = right - left + 1
            
            # If replacements needed > k, shrink window
            if window_size - max_char_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update max length (window is always valid here)
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    @staticmethod
    def find_all_anagrams(s: str, p: str) -> List[int]:
        """
        Find all start indices of anagrams of p in s.
        
        Time: O(|s|), Space: O(1) - at most 26 characters
        
        Template for: Fixed window with anagram detection
        """
        if len(p) > len(s):
            return []
        
        result = []
        p_count = Counter(p)
        window_count = Counter()
        
        # Process first window
        for i in range(len(p)):
            window_count[s[i]] += 1
        
        # Check first window
        if window_count == p_count:
            result.append(0)
        
        # Slide window
        for i in range(len(p), len(s)):
            # Add new character
            window_count[s[i]] += 1
            
            # Remove old character
            left_char = s[i - len(p)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Check if current window is anagram
            if window_count == p_count:
                result.append(i - len(p) + 1)
        
        return result


# Generic sliding window templates
def sliding_window_fixed_size(arr: List[int], k: int, operation_func):
    """
    Generic template for fixed-size sliding window problems.
    
    Args:
        arr: Input array
        k: Window size
        operation_func: Function to apply on each window
    
    Returns:
        Result based on operation_func
    """
    if len(arr) < k:
        return None
    
    # Initialize first window
    result = operation_func(arr[:k])
    
    # Slide window
    for i in range(k, len(arr)):
        # Remove leftmost, add rightmost
        window = arr[i-k+1:i+1]
        current_result = operation_func(window)
        result = max(result, current_result)  # or min, or other operation
=======
def max_sum_subarray_size_k(nums: List[int], k: int) -> int:
    """
    Find maximum sum of subarray of size k.
    
    Args:
        nums: Array of integers
        k: Size of subarray
        
    Returns:
        Maximum sum of subarray of size k
        
    Time: O(n), Space: O(1)
    """
    if len(nums) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        # Remove leftmost element, add rightmost element
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def longest_substring_without_repeating(s: str) -> int:
    """
    Find length of longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
        
    Time: O(n), Space: O(min(m, n)) where m is charset size
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is repeated and within current window
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find length of longest substring with at most k distinct characters.
    
    Args:
        s: Input string
        k: Maximum number of distinct characters
        
    Returns:
        Length of longest valid substring
        
    Time: O(n), Space: O(k)
    """
    if k == 0:
        return 0
    
    char_count = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # Add character to window
        char_count[char] = char_count.get(char, 0) + 1
        
        # Shrink window if too many distinct characters
        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length


def min_window_substring(s: str, t: str) -> str:
    """
    Find minimum window substring that contains all characters of t.
    
    Args:
        s: Source string
        t: Target string (characters to find)
        
    Returns:
        Minimum window substring, empty string if not found
        
    Time: O(|s| + |t|), Space: O(|s| + |t|)
    """
    if not s or not t:
        return ""
    
    # Count characters in t
    dict_t = Counter(t)
    required = len(dict_t)
    
    # Sliding window variables
    left = right = 0
    formed = 0  # Number of unique chars in current window with desired frequency
    
    # Dictionary to keep count of characters in current window
    window_counts = {}
    
    # Result
    min_len = float('inf')
    min_left = 0
    
    while right < len(s):
        # Add character from right to window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if frequency matches requirement
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        # Try to contract window until it's no longer valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update result if this window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            
            # Remove character from left
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if min_len == float('inf') else s[min_left:min_left + min_len]


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    Count number of continuous subarrays whose sum equals k.
    
    Args:
        nums: Array of integers
        k: Target sum
        
    Returns:
        Number of subarrays with sum k
        
    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Handle case where prefix_sum == k
    
    for num in nums:
        prefix_sum += num
        
        # Check if there's a prefix sum such that current - prefix = k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Add current prefix sum to map
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


def max_consecutive_ones_k_flips(nums: List[int], k: int) -> int:
    """
    Find maximum consecutive 1s after flipping at most k zeros.
    
    Args:
        nums: Binary array (0s and 1s)
        k: Maximum number of 0s that can be flipped
        
    Returns:
        Maximum length of consecutive 1s
        
    Time: O(n), Space: O(1)
    """
    left = 0
    max_length = 0
    zeros_count = 0
    
    for right in range(len(nums)):
        # Expand window
        if nums[right] == 0:
            zeros_count += 1
        
        # Contract window if too many zeros
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


def character_replacement(s: str, k: int) -> int:
    """
    Find longest substring with same characters after k replacements.
    
    Args:
        s: Input string
        k: Maximum number of character replacements
        
    Returns:
        Length of longest valid substring
        
    Time: O(n), Space: O(1) - at most 26 characters
    """
    char_count = {}
    max_length = 0
    max_count = 0
    start = 0
    
    for end in range(len(s)):
        # Add character to window
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        max_count = max(max_count, char_count[s[end]])
        
        # If window size - max_count > k, shrink window
        if end - start + 1 - max_count > k:
            char_count[s[start]] -= 1
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length


def find_all_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of anagrams of p in s.
    
    Args:
        s: Source string
        p: Pattern string
        
    Returns:
        List of starting indices where anagrams are found
        
    Time: O(|s|), Space: O(1) - at most 26 characters
    """
    if len(p) > len(s):
        return []
    
    result = []
    p_count = Counter(p)
    window_count = Counter()
    
    # Initialize first window
    for i in range(len(p)):
        window_count[s[i]] += 1
    
    # Check first window
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Remove old character
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
>>>>>>> 173ecd5 (wip)
    
    return result


<<<<<<< HEAD
def sliding_window_variable_size(arr: List[int], condition_func):
    """
    Generic template for variable-size sliding window problems.
    
    Args:
        arr: Input array
        condition_func: Function that returns True if window is valid
    
=======
# Template for sliding window problems
def sliding_window_template(s: str, is_valid_func) -> int:
    """
    Generic template for sliding window problems.
    
    Args:
        s: Input string/array
        is_valid_func: Function that takes window state and returns if valid
        
>>>>>>> 173ecd5 (wip)
    Returns:
        Maximum valid window size
    """
    left = 0
    max_size = 0
<<<<<<< HEAD
    
    for right in range(len(arr)):
        # Expand window by including arr[right]
        
        # Shrink window while condition is violated
        while not condition_func(arr[left:right+1]):
            left += 1
        
        # Update maximum size
=======
    window_state = {}
    
    for right in range(len(s)):
        # Expand window
        char = s[right]
        window_state[char] = window_state.get(char, 0) + 1
        
        # Contract window while invalid
        while not is_valid_func(window_state):
            left_char = s[left]
            window_state[left_char] -= 1
            if window_state[left_char] == 0:
                del window_state[left_char]
            left += 1
        
>>>>>>> 173ecd5 (wip)
        max_size = max(max_size, right - left + 1)
    
    return max_size


<<<<<<< HEAD
# Interview tips and common patterns
"""
Sliding Window Interview Tips:

1. **When to use:**
   - Subarray/substring problems
   - Contiguous sequence problems
   - Problems with size constraints
   - Optimization problems (min/max)

2. **Two main types:**
   - Fixed size: Window size is constant
   - Variable size: Window size changes based on conditions

3. **Key patterns:**
   - Expand window: Add elements to right
   - Shrink window: Remove elements from left
   - Update result: Track optimal solution

4. **Common optimizations:**
   - Use hashmaps for character/element counting
   - Track maximum frequency for efficiency
   - Use deque for min/max in window

5. **Edge cases:**
   - Empty input
   - Window size larger than input
   - No valid window exists
   - Single element arrays

6. **Python techniques:**
   - Counter for frequency counting
   - defaultdict for automatic initialization
   - Deque for efficient front/back operations
   - Set operations for uniqueness checks

7. **Time complexity:**
   - Usually O(n) where n is input size
   - Each element visited at most twice (left and right pointers)
=======
# Interview Tips and Common Patterns
"""
Sliding Window Interview Tips:

1. **When to Use**:
   - Problems involving subarrays/substrings
   - Looking for optimal window (min/max size)
   - Constraints on window contents (sum, distinct chars, etc.)
   - Can avoid nested loops (O(n²) → O(n))

2. **Two Main Types**:
   - Fixed Size Window: Window size is given
   - Variable Size Window: Find optimal window size

3. **Key Patterns**:
   - Expand window by moving right pointer
   - Contract window by moving left pointer
   - Use hash map to track window contents
   - Update result when window is valid

4. **Python Optimizations**:
   - Use collections.Counter for frequency counting
   - Use collections.defaultdict to avoid key checks
   - Leverage enumerate() for index tracking
   - Use get() method with default values

5. **Common Mistakes**:
   - Not handling edge cases (empty input, k=0)
   - Incorrect window contraction logic
   - Not updating result at the right time
   - Memory leaks in hash maps (not removing zero counts)

6. **Template Structure**:
   ```python
   left = 0
   for right in range(len(arr)):
       # Expand window
       add arr[right] to window
       
       # Contract window while invalid
       while window is invalid:
           remove arr[left] from window
           left += 1
       
       # Update result
       update max/min result
   ```
>>>>>>> 173ecd5 (wip)
"""