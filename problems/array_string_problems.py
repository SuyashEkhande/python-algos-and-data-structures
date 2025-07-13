"""
Array and String Problems

This module contains solutions to common coding interview problems
involving arrays and strings from platforms like LeetCode, HackerRank, etc.
"""


def two_sum(nums, target):
    """
    LeetCode #1: Two Sum
    Given an array of integers, return indices of two numbers that add up to target.
    
    Time: O(n), Space: O(n)
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


def three_sum(nums):
    """
    LeetCode #15: 3Sum
    Find all unique triplets that sum to zero.
    
    Time: O(n²), Space: O(1)
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicates
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


def container_with_most_water(height):
    """
    LeetCode #11: Container With Most Water
    Find two lines that form container holding the most water.
    
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def longest_substring_without_repeating(s):
    """
    LeetCode #3: Longest Substring Without Repeating Characters
    Find length of longest substring without repeating characters.
    
    Time: O(n), Space: O(min(m,n)) where m is charset size
    """
    char_map = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def longest_palindromic_substring(s):
    """
    LeetCode #5: Longest Palindromic Substring
    Find the longest palindromic substring.
    
    Time: O(n²), Space: O(1)
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]


def group_anagrams(strs):
    """
    LeetCode #49: Group Anagrams
    Group strings that are anagrams of each other.
    
    Time: O(n * k log k), Space: O(n * k)
    """
    anagram_map = {}
    
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
    
    return list(anagram_map.values())


def valid_parentheses(s):
    """
    LeetCode #20: Valid Parentheses
    Check if string has valid parentheses.
    
    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack


def longest_common_prefix(strs):
    """
    LeetCode #14: Longest Common Prefix
    Find longest common prefix among array of strings.
    
    Time: O(S) where S is sum of all characters, Space: O(1)
    """
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    
    return strs[0]


def string_to_integer_atoi(s):
    """
    LeetCode #8: String to Integer (atoi)
    Convert string to 32-bit signed integer.
    
    Time: O(n), Space: O(1)
    """
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    i = 0
    
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        i = 1
    
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    result *= sign
    
    # Handle 32-bit integer overflow
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    return max(INT_MIN, min(INT_MAX, result))


def zigzag_conversion(s, numRows):
    """
    LeetCode #6: ZigZag Conversion
    Convert string to zigzag pattern and read line by line.
    
    Time: O(n), Space: O(n)
    """
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [''] * numRows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        current_row += 1 if going_down else -1
    
    return ''.join(rows)


def rotate_array(nums, k):
    """
    LeetCode #189: Rotate Array
    Rotate array to the right by k steps.
    
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


def product_except_self(nums):
    """
    LeetCode #238: Product of Array Except Self
    Return array where each element is product of all elements except itself.
    
    Time: O(n), Space: O(1) excluding output array
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate left products
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    
    # Calculate right products and combine
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result


def find_minimum_in_rotated_sorted_array(nums):
    """
    LeetCode #153: Find Minimum in Rotated Sorted Array
    Find minimum element in rotated sorted array.
    
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]


def maximum_subarray(nums):
    """
    LeetCode #53: Maximum Subarray (Kadane's Algorithm)
    Find contiguous subarray with largest sum.
    
    Time: O(n), Space: O(1)
    """
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def merge_intervals(intervals):
    """
    LeetCode #56: Merge Intervals
    Merge overlapping intervals.
    
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            # Overlapping intervals, merge them
            merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:
            # Non-overlapping interval, add to result
            merged.append(current)
    
    return merged


# Example usage and test cases
if __name__ == "__main__":
    print("=== Array and String Problems Solutions ===")
    
    # Two Sum
    print("\n1. Two Sum:")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Array: {nums}, Target: {target}")
    print(f"Indices: {result}")
    
    # Three Sum
    print("\n2. Three Sum:")
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print(f"Array: {nums}")
    print(f"Triplets that sum to 0: {result}")
    
    # Container With Most Water
    print("\n3. Container With Most Water:")
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = container_with_most_water(height)
    print(f"Heights: {height}")
    print(f"Maximum water area: {result}")
    
    # Longest Substring Without Repeating
    print("\n4. Longest Substring Without Repeating:")
    s = "abcabcbb"
    result = longest_substring_without_repeating(s)
    print(f"String: '{s}'")
    print(f"Length of longest substring: {result}")
    
    # Longest Palindromic Substring
    print("\n5. Longest Palindromic Substring:")
    s = "babad"
    result = longest_palindromic_substring(s)
    print(f"String: '{s}'")
    print(f"Longest palindrome: '{result}'")
    
    # Group Anagrams
    print("\n6. Group Anagrams:")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    print(f"Strings: {strs}")
    print(f"Grouped anagrams: {result}")
    
    # Valid Parentheses
    print("\n7. Valid Parentheses:")
    s = "()[]{}"
    result = valid_parentheses(s)
    print(f"String: '{s}'")
    print(f"Valid: {result}")
    
    # Product Except Self
    print("\n8. Product Except Self:")
    nums = [1, 2, 3, 4]
    result = product_except_self(nums)
    print(f"Array: {nums}")
    print(f"Product except self: {result}")
    
    # Maximum Subarray
    print("\n9. Maximum Subarray:")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maximum_subarray(nums)
    print(f"Array: {nums}")
    print(f"Maximum subarray sum: {result}")
    
    # Merge Intervals
    print("\n10. Merge Intervals:")
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge_intervals(intervals)
    print(f"Intervals: {intervals}")
    print(f"Merged intervals: {result}")
    
    print(f"\nNote: These are classic coding interview problems")
    print("Each solution includes optimal time/space complexity")
    print("and handles edge cases appropriately.")