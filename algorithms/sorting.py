"""
Sorting Algorithms Implementation

This module contains various sorting algorithms with their implementations,
time complexity analysis, and usage examples.
"""

import random
import time


def bubble_sort(arr):
    """
    Bubble Sort - O(n²) time complexity
    Repeatedly steps through the list, compares adjacent elements and swaps them if needed.
    """
    arr = arr.copy()  # Don't modify original array
    n = len(arr)
    
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr


def selection_sort(arr):
    """
    Selection Sort - O(n²) time complexity
    Finds the minimum element and places it at the beginning.
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        # Find minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr):
    """
    Insertion Sort - O(n²) time complexity, O(n) best case
    Builds the final sorted array one item at a time.
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr):
    """
    Merge Sort - O(n log n) time complexity
    Divide and conquer algorithm that divides array into halves and merges them.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr):
    """
    Quick Sort - O(n log n) average, O(n²) worst case
    Picks a pivot and partitions array around it.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place Quick Sort implementation.
    More memory efficient version of quick sort.
    """
    if high is None:
        high = len(arr) - 1
        arr = arr.copy()  # Don't modify original
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """Partition function for in-place quick sort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr):
    """
    Heap Sort - O(n log n) time complexity
    Uses binary heap data structure to sort elements.
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)  # Call heapify on reduced heap
    
    return arr


def heapify(arr, n, i):
    """Helper function to maintain heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr, max_val=None):
    """
    Counting Sort - O(n + k) time complexity
    Efficient for sorting when range of input is known and small.
    """
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    
    # Count array to store count of each element
    count = [0] * (max_val + 1)
    
    # Store count of each element
    for num in arr:
        count[num] += 1
    
    # Build result array
    result = []
    for i, cnt in enumerate(count):
        result.extend([i] * cnt)
    
    return result


def radix_sort(arr):
    """
    Radix Sort - O(d * n) time complexity
    Sorts by processing individual digits.
    """
    if not arr:
        return arr
    
    arr = arr.copy()
    max_num = max(arr)
    
    # Process each digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_by_digit(arr, exp):
    """Helper function for radix sort - counting sort by digit."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Change count[i] to actual position of this digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]


def bucket_sort(arr, num_buckets=10):
    """
    Bucket Sort - O(n + k) average case
    Distributes elements into buckets and sorts them individually.
    """
    if not arr:
        return arr
    
    # Find min and max values
    min_val, max_val = min(arr), max(arr)
    
    # Create buckets
    bucket_range = (max_val - min_val) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        if num == max_val:
            bucket_index = num_buckets - 1
        else:
            bucket_index = int((num - min_val) / bucket_range)
        buckets[bucket_index].append(num)
    
    # Sort individual buckets and concatenate
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))
    
    return result


def is_sorted(arr):
    """Check if array is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def benchmark_sorting_algorithms(arr_size=1000):
    """Benchmark different sorting algorithms."""
    # Generate random array
    test_array = [random.randint(1, 1000) for _ in range(arr_size)]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", lambda arr: counting_sort(arr, 1000)),
        ("Radix Sort", radix_sort),
        ("Bucket Sort", bucket_sort),
    ]
    
    print(f"Benchmarking sorting algorithms on array of size {arr_size}")
    print("-" * 50)
    
    for name, algorithm in algorithms:
        start_time = time.time()
        
        try:
            sorted_arr = algorithm(test_array)
            end_time = time.time()
            
            # Verify correctness
            if is_sorted(sorted_arr) and len(sorted_arr) == len(test_array):
                print(f"{name:15}: {end_time - start_time:.6f} seconds ✓")
            else:
                print(f"{name:15}: INCORRECT RESULT ✗")
        
        except Exception as e:
            print(f"{name:15}: ERROR - {e}")


# Example usage and demonstrations
if __name__ == "__main__":
    # Test array
    test_array = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original array: {test_array}")
    print()
    
    # Test all sorting algorithms
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Quick Sort (In-place)", quick_sort_inplace),
        ("Heap Sort", heap_sort),
        ("Counting Sort", lambda arr: counting_sort(arr, max(arr))),
        ("Radix Sort", radix_sort),
        ("Bucket Sort", bucket_sort),
    ]
    
    for name, algorithm in algorithms:
        sorted_arr = algorithm(test_array)
        print(f"{name:20}: {sorted_arr}")
    
    print()
    
    # Benchmark with larger array
    print("=== Performance Benchmark ===")
    benchmark_sorting_algorithms(100)  # Small array for demo
    
    print("\n=== Stability Test ===")
    # Test with array containing duplicates to check stability
    stable_test = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
    print(f"Original (value, label): {stable_test}")
    
    # For demo, just show which algorithms preserve relative order of equal elements
    print("Note: Stable algorithms preserve relative order of equal elements")
    print("Stable: Bubble, Insertion, Merge, Counting, Radix, Bucket")
    print("Unstable: Selection, Quick, Heap")