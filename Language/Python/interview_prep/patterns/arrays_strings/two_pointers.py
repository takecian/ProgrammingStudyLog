"""
Two Pointers Pattern for Arrays and Strings

The two pointers technique is a common pattern used to solve array and string problems efficiently.
It involves using two pointers that move through the data structure, often from opposite ends
or at different speeds, to find a solution in O(n) time complexity.

Common use cases:
- Finding pairs with a target sum in sorted arrays
- Palindrome checking
- Removing duplicates
- Container with most water problems
- Trapping rainwater
"""

from typing import List, Optional, Tuple


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
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
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
"""