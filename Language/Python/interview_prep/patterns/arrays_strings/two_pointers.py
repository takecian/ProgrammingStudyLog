"""
Two Pointers Pattern - Array and String Manipulation

Common patterns for solving array and string problems efficiently using two pointers.
Time Complexity: Usually O(n), Space Complexity: Usually O(1)
"""

from typing import List, Optional, Tuple


def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Find two numbers in sorted array that add up to target."""
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
    """Check if string is palindrome using two pointers."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


def remove_duplicates(nums: List[int]) -> int:
    """Remove duplicates from sorted array in-place."""
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


def container_with_most_water(height: List[int]) -> int:
    """Find container that can hold most water."""
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def three_sum(nums: List[int]) -> List[List[int]]:
    """Find all unique triplets that sum to zero."""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
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
    """Sort array of 0s, 1s, 2s in-place (Dutch National Flag)."""
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