"""
Searching Algorithms Implementation

This module contains various searching algorithms including linear search,
binary search, and their variations with complexity analysis.
"""

import math


def linear_search(arr, target):
    """
    Linear Search - O(n) time complexity
    Searches for target by checking each element sequentially.
    
    Args:
        arr: List of elements to search in
        target: Element to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search - O(log n) time complexity
    Searches for target in sorted array by repeatedly dividing search space in half.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
    
    Returns:
        Index of target if found, -1 otherwise
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


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive Binary Search - O(log n) time complexity
    Recursive implementation of binary search.
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_leftmost(arr, target):
    """
    Find leftmost occurrence of target in sorted array with duplicates.
    Returns the index of first occurrence, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_rightmost(arr, target):
    """
    Find rightmost occurrence of target in sorted array with duplicates.
    Returns the index of last occurrence, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_range(arr, target):
    """
    Find the range [start, end] of target in sorted array.
    Returns tuple (start_index, end_index) or (-1, -1) if not found.
    """
    left = binary_search_leftmost(arr, target)
    if left == -1:
        return (-1, -1)
    
    right = binary_search_rightmost(arr, target)
    return (left, right)


def interpolation_search(arr, target):
    """
    Interpolation Search - O(log log n) for uniformly distributed data
    Improves binary search by estimating position based on value.
    Works best with uniformly distributed sorted arrays.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # If array has only one element
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Estimate position using interpolation formula
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


def exponential_search(arr, target):
    """
    Exponential Search - O(log n) time complexity
    Finds range for binary search by repeatedly doubling the index.
    Useful when array size is unknown or very large.
    """
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Perform binary search in the found range
    return binary_search_in_range(arr, target, i // 2, min(i, len(arr) - 1))


def binary_search_in_range(arr, target, left, right):
    """Helper function for binary search in a specific range."""
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def jump_search(arr, target):
    """
    Jump Search - O(√n) time complexity
    Searches by jumping ahead by fixed steps, then linear search in block.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Finding the block where element may be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the identified block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    # If element is found
    if arr[prev] == target:
        return prev
    
    return -1


def ternary_search(arr, target, left=0, right=None):
    """
    Ternary Search - O(log₃ n) time complexity
    Divides array into three parts instead of two like binary search.
    """
    if right is None:
        right = len(arr) - 1
    
    if right >= left:
        # Divide the array into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Target is in first third
        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        # Target is in last third
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        # Target is in middle third
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)
    
    return -1


def fibonacci_search(arr, target):
    """
    Fibonacci Search - O(log n) time complexity
    Uses Fibonacci numbers to divide the array into unequal parts.
    """
    n = len(arr)
    
    # Initialize Fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number
    
    # Find smallest Fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    # Marks the eliminated range from front
    offset = -1
    
    # While there are elements to be inspected
    while fib_m > 1:
        # Check if fib_m2 is a valid location
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    # Compare the last element
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1


def find_peak_element(arr):
    """
    Find peak element in array using binary search.
    Peak element is greater than its neighbors.
    O(log n) time complexity.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left


def search_in_rotated_array(arr, target):
    """
    Search in rotated sorted array using modified binary search.
    O(log n) time complexity.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check which half is sorted
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


def find_minimum_in_rotated_array(arr):
    """
    Find minimum element in rotated sorted array.
    O(log n) time complexity.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left


# Example usage and demonstrations
if __name__ == "__main__":
    # Test arrays
    linear_array = [64, 34, 25, 12, 22, 11, 90, 5]
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    duplicate_array = [1, 2, 2, 2, 3, 4, 4, 5]
    rotated_array = [4, 5, 6, 7, 0, 1, 2]
    
    print("=== Linear Search ===")
    target = 22
    result = linear_search(linear_array, target)
    print(f"Array: {linear_array}")
    print(f"Searching for {target}: Index {result}")
    
    print("\n=== Binary Search ===")
    target = 7
    result = binary_search(sorted_array, target)
    print(f"Sorted array: {sorted_array}")
    print(f"Searching for {target}: Index {result}")
    
    print("\n=== Binary Search with Duplicates ===")
    target = 2
    leftmost = binary_search_leftmost(duplicate_array, target)
    rightmost = binary_search_rightmost(duplicate_array, target)
    range_result = binary_search_range(duplicate_array, target)
    print(f"Array with duplicates: {duplicate_array}")
    print(f"Searching for {target}:")
    print(f"  Leftmost index: {leftmost}")
    print(f"  Rightmost index: {rightmost}")
    print(f"  Range: {range_result}")
    
    print("\n=== Advanced Search Algorithms ===")
    target = 7
    
    # Test different search algorithms
    algorithms = [
        ("Binary Search Recursive", lambda: binary_search_recursive(sorted_array, target)),
        ("Interpolation Search", lambda: interpolation_search(sorted_array, target)),
        ("Exponential Search", lambda: exponential_search(sorted_array, target)),
        ("Jump Search", lambda: jump_search(sorted_array, target)),
        ("Ternary Search", lambda: ternary_search(sorted_array, target)),
        ("Fibonacci Search", lambda: fibonacci_search(sorted_array, target)),
    ]
    
    print(f"Searching for {target} in {sorted_array}:")
    for name, search_func in algorithms:
        result = search_func()
        print(f"  {name:25}: Index {result}")
    
    print("\n=== Special Cases ===")
    
    # Peak element
    peak_array = [1, 3, 20, 4, 1, 0]
    peak_index = find_peak_element(peak_array)
    print(f"Peak element in {peak_array}: Index {peak_index} (value: {peak_array[peak_index]})")
    
    # Search in rotated array
    target = 0
    rotated_result = search_in_rotated_array(rotated_array, target)
    print(f"Search {target} in rotated array {rotated_array}: Index {rotated_result}")
    
    # Find minimum in rotated array
    min_index = find_minimum_in_rotated_array(rotated_array)
    print(f"Minimum in rotated array {rotated_array}: Index {min_index} (value: {rotated_array[min_index]})")
    
    print("\n=== Performance Comparison ===")
    import time
    large_array = list(range(0, 10000, 2))  # Even numbers 0 to 9998
    target = 5000
    
    search_algorithms = [
        ("Linear Search", lambda: linear_search(large_array, target)),
        ("Binary Search", lambda: binary_search(large_array, target)),
        ("Interpolation Search", lambda: interpolation_search(large_array, target)),
        ("Jump Search", lambda: jump_search(large_array, target)),
    ]
    
    print(f"Searching for {target} in array of size {len(large_array)}:")
    for name, search_func in search_algorithms:
        start_time = time.time()
        result = search_func()
        end_time = time.time()
        print(f"  {name:20}: {end_time - start_time:.6f} seconds (Index: {result})")