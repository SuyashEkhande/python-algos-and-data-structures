"""
Array Data Structure Implementation and Operations

This module contains various array operations and algorithms commonly used in DSA.
"""


class DynamicArray:
    """A dynamic array implementation similar to Python's list."""
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")
    
    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")
    
    def append(self, value):
        """Add element to the end of array."""
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """Insert element at given index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if self.size >= self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def delete(self, index):
        """Delete element at given index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
    
    def _resize(self):
        """Double the capacity when array is full."""
        old_data = self.data
        self.capacity *= 2
        self.data = [None] * self.capacity
        
        for i in range(self.size):
            self.data[i] = old_data[i]


def find_max_subarray_sum(arr):
    """
    Kadane's Algorithm to find maximum subarray sum.
    Time Complexity: O(n)
    """
    if not arr:
        return 0
    
    max_sum = current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def rotate_array(arr, k):
    """
    Rotate array to the right by k steps.
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not arr or k == 0:
        return arr
    
    n = len(arr)
    k = k % n  # Handle k > n
    
    # Reverse entire array
    reverse_array(arr, 0, n - 1)
    # Reverse first k elements
    reverse_array(arr, 0, k - 1)
    # Reverse remaining elements
    reverse_array(arr, k, n - 1)
    
    return arr


def reverse_array(arr, start, end):
    """Helper function to reverse array between start and end indices."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def two_sum(arr, target):
    """
    Find two numbers in array that sum to target.
    Returns indices of the two numbers.
    Time Complexity: O(n)
    """
    num_map = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return None


def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in-place.
    Returns new length of array.
    """
    if not arr:
        return 0
    
    write_index = 1
    
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return write_index


# Example usage and demonstrations
if __name__ == "__main__":
    # Dynamic Array example
    print("=== Dynamic Array Example ===")
    arr = DynamicArray(5)
    for i in range(1, 6):
        arr.append(i * 10)
    print(f"Array after adding 5 elements: {[arr[i] for i in range(len(arr))]}")
    
    arr.insert(2, 25)
    print(f"After inserting 25 at index 2: {[arr[i] for i in range(len(arr))]}")
    
    # Maximum subarray sum example
    print("\n=== Maximum Subarray Sum (Kadane's Algorithm) ===")
    test_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = find_max_subarray_sum(test_arr)
    print(f"Array: {test_arr}")
    print(f"Maximum subarray sum: {max_sum}")
    
    # Array rotation example
    print("\n=== Array Rotation ===")
    test_arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Original array: {test_arr}")
    rotated = rotate_array(test_arr.copy(), k)
    print(f"Rotated by {k} positions: {rotated}")
    
    # Two sum example
    print("\n=== Two Sum Problem ===")
    test_arr = [2, 7, 11, 15]
    target = 9
    result = two_sum(test_arr, target)
    print(f"Array: {test_arr}, Target: {target}")
    print(f"Indices that sum to target: {result}")