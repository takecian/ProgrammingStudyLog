"""
Sliding Window Pattern for Arrays and Strings

The sliding window technique is used to solve problems involving subarrays or substrings
by maintaining a window that slides through the data structure. This pattern is particularly
effective for problems involving contiguous sequences.

Common use cases:
- Maximum/minimum subarray problems
- Substring problems with constraints
- Finding patterns in strings
- Fixed or variable window size problems
"""

from typing import List, Dict, Optional
from collections import defaultdict, Counter


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
    
    return result


def sliding_window_variable_size(arr: List[int], condition_func):
    """
    Generic template for variable-size sliding window problems.
    
    Args:
        arr: Input array
        condition_func: Function that returns True if window is valid
    
    Returns:
        Maximum valid window size
    """
    left = 0
    max_size = 0
    
    for right in range(len(arr)):
        # Expand window by including arr[right]
        
        # Shrink window while condition is violated
        while not condition_func(arr[left:right+1]):
            left += 1
        
        # Update maximum size
        max_size = max(max_size, right - left + 1)
    
    return max_size


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
"""