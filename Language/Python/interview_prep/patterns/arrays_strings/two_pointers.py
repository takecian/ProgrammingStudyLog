"""
<<<<<<< HEAD
Two Pointers Pattern for Arrays and Strings

The two pointers technique is a common pattern used to solve array and string problems efficiently.
It involves using two pointers that move through the data structure, often from opposite ends
or at different speeds, to find a solution in O(n) time complexity.

Common use cases:
- Finding pairs with a target sum in sorted arrays
- Palindrome checking
- Removing duplicates
- Container with most water problems
=======
Two Pointers Pattern - Array and String Manipulation

This module contains implementations and templates for the two-pointer technique,
a fundamental pattern for solving array and string problems efficiently.

Time Complexity: Usually O(n)
Space Complexity: Usually O(1)

Common Use Cases:
- Finding pairs with target sum
- Removing duplicates from sorted arrays
- Palindrome checking
- Container with most water
>>>>>>> 173ecd5 (wip)
- Trapping rainwater
"""

from typing import List, Optional, Tuple


<<<<<<< HEAD
class TwoPointersPatterns:
    """Collection of two pointers pattern implementations and templates."""
    
    @staticmethod
    def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        """
        Find two numbers in a sorted array that add up to target.
        
        Time: O(n), Space: O(1)
        
        Template for: Two sum in sorted array, pair finding problems
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                return (left, right)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return None
    
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Check if string is a palindrome using two pointers.
        
        Time: O(n), Space: O(1)
        
        Template for: Palindrome checking, string validation
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.
        
        Time: O(n), Space: O(1)
        
        Template for: In-place array modification, duplicate removal
        """
        if not nums:
            return 0
        
        # Two pointers: slow for unique elements, fast for scanning
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1
    
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.
        
        Time: O(n²), Space: O(1) excluding output
        
        Template for: Three sum, multiple pointer problems
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    @staticmethod
    def container_with_most_water(heights: List[int]) -> int:
        """
        Find container that can hold the most water.
        
        Time: O(n), Space: O(1)
        
        Template for: Area maximization, greedy two pointers
        """
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(max_area, area)
            
            # Move pointer with smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    @staticmethod
    def reverse_words_in_string(s: str) -> str:
        """
        Reverse words in a string using two pointers approach.
        
        Time: O(n), Space: O(n) for result
        
        Template for: String reversal, word manipulation
        """
        # Convert to list for in-place operations
        chars = list(s.strip())
        
        # Helper function to reverse portion of array
        def reverse(start: int, end: int):
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        
        # Remove extra spaces
        write_idx = 0
        for read_idx in range(len(chars)):
            if chars[read_idx] != ' ':
                if write_idx != 0:
                    chars[write_idx] = ' '
                    write_idx += 1
                
                while read_idx < len(chars) and chars[read_idx] != ' ':
                    chars[write_idx] = chars[read_idx]
                    write_idx += 1
                    read_idx += 1
        
        chars = chars[:write_idx]
        
        # Reverse entire string
        reverse(0, len(chars) - 1)
        
        # Reverse each word
        start = 0
        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == ' ':
                reverse(start, i - 1)
                start = i + 1
        
        return ''.join(chars)


# Template for custom two pointers problems
def two_pointers_template(arr: List[int], condition_func) -> bool:
    """
    Generic two pointers template.
    
    Args:
        arr: Input array
        condition_func: Function that takes (left_val, right_val) and returns comparison result
    
    Returns:
        Boolean result based on condition
=======
def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers in a sorted array that add up to target.
    
    Args:
        nums: Sorted array of integers
        target: Target sum
        
    Returns:
        Tuple of indices (i, j) if found, None otherwise
        
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using two pointers.
    
    Args:
        s: Input string
        
    Returns:
        True if palindrome, False otherwise
        
    Time: O(n), Space: O(1)
    """
    # Clean string: keep only alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        nums: Sorted array with duplicates
        
    Returns:
        Length of array after removing duplicates
        
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    # Slow pointer tracks position for next unique element
    slow = 0
    
    # Fast pointer explores the array
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def container_with_most_water(height: List[int]) -> int:
    """
    Find container that can hold the most water.
    
    Args:
        height: Array of heights
        
    Returns:
        Maximum area of water that can be contained
        
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: Array of integers
        
    Returns:
        List of triplets that sum to zero
        
    Time: O(n²), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second and third numbers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result


def sort_colors(nums: List[int]) -> None:
    """
    Sort array of 0s, 1s, and 2s in-place (Dutch National Flag).
    
    Args:
        nums: Array containing only 0, 1, 2
        
    Time: O(n), Space: O(1)
    """
    # Three pointers: left (0s), current (processing), right (2s)
    left = current = 0
    right = len(nums) - 1
    
    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 1:
            current += 1
        else:  # nums[current] == 2
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
            # Don't increment current as we need to check swapped element


def reverse_words_in_string(s: str) -> str:
    """
    Reverse words in a string using two pointers approach.
    
    Args:
        s: Input string with words separated by spaces
        
    Returns:
        String with words in reverse order
        
    Time: O(n), Space: O(n) for result
    """
    # Convert to list for in-place manipulation
    chars = list(s.strip())
    
    # Helper function to reverse substring
    def reverse_substring(start: int, end: int):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
    
    # First, reverse the entire string
    reverse_substring(0, len(chars) - 1)
    
    # Then reverse each word
    start = 0
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == ' ':
            reverse_substring(start, i - 1)
            start = i + 1
    
    return ''.join(chars)


# Template for two-pointer problems
def two_pointer_template(arr: List[int], condition_func) -> Optional[Tuple[int, int]]:
    """
    Generic template for two-pointer problems.
    
    Args:
        arr: Input array
        condition_func: Function that takes (left_val, right_val) and returns:
                       -1 if need to move left pointer
                        0 if found solution
                        1 if need to move right pointer
    
    Returns:
        Tuple of indices if solution found, None otherwise
>>>>>>> 173ecd5 (wip)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
<<<<<<< HEAD
        left_val, right_val = arr[left], arr[right]
        
        result = condition_func(left_val, right_val)
        
        if result == 0:  # Found target
            return True
        elif result < 0:  # Need larger sum
            left += 1
        else:  # Need smaller sum
            right -= 1
    
    return False


# Interview tips and common patterns
"""
Two Pointers Interview Tips:

1. **When to use:**
   - Sorted array problems
   - Palindrome checking
   - Finding pairs/triplets
   - In-place array modifications
   - String reversal problems

2. **Common variations:**
   - Opposite ends (left=0, right=n-1)
   - Same direction (slow/fast pointers)
   - Multiple pointers (three sum, four sum)

3. **Key insights:**
   - Often reduces O(n²) to O(n)
   - Works well with sorted data
   - Can eliminate need for extra space
   - Greedy approach: move pointer that helps progress

4. **Edge cases to consider:**
   - Empty arrays/strings
   - Single element
   - All elements same
   - No valid solution exists

5. **Python optimizations:**
   - Use while loops instead of for loops for flexibility
   - Leverage string methods: isalnum(), lower()
   - List slicing for subarrays: arr[left:right+1]
   - Built-in functions: min(), max(), sum()
=======
        result = condition_func(arr[left], arr[right])
        
        if result == 0:
            return (left, right)
        elif result < 0:
            left += 1
        else:
            right -= 1
    
    return None


# Interview Tips and Common Patterns
"""
Two Pointers Interview Tips:

1. **When to Use**:
   - Array/string is sorted or can be sorted
   - Looking for pairs/triplets with specific properties
   - Need to process from both ends toward center
   - Want to avoid nested loops (O(n²) → O(n))

2. **Common Variations**:
   - Same direction (fast/slow pointers)
   - Opposite direction (left/right pointers)
   - Multiple arrays (merge sorted arrays)

3. **Key Insights**:
   - Always consider what moving each pointer means
   - Handle duplicates carefully in sum problems
   - Use while loops with clear termination conditions
   - Consider edge cases (empty array, single element)

4. **Python Optimizations**:
   - Use tuple unpacking for swaps: a, b = b, a
   - Leverage list slicing when appropriate
   - Use enumerate() for index tracking
   - Consider using collections.deque for queue operations

5. **Common Mistakes**:
   - Not handling duplicates in sum problems
   - Infinite loops due to incorrect pointer movement
   - Off-by-one errors in boundary conditions
   - Not considering empty or single-element inputs
>>>>>>> 173ecd5 (wip)
"""