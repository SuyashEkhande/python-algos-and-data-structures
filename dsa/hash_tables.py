"""
Hash Table (Dictionary) Implementation

This module contains hash table implementation with various collision resolution strategies.
"""


class HashTable:
    """Hash table implementation using separate chaining for collision resolution."""
    
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key):
        """Simple hash function using built-in hash."""
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """Insert or update key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor exceeds threshold
        if self.size >= self.capacity * 0.75:
            self._resize()
    
    def get(self, key):
        """Get value for given key."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Check if key exists in hash table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def keys(self):
        """Return all keys."""
        all_keys = []
        for bucket in self.buckets:
            for k, v in bucket:
                all_keys.append(k)
        return all_keys
    
    def values(self):
        """Return all values."""
        all_values = []
        for bucket in self.buckets:
            for k, v in bucket:
                all_values.append(v)
        return all_values
    
    def items(self):
        """Return all key-value pairs."""
        all_items = []
        for bucket in self.buckets:
            for item in bucket:
                all_items.append(item)
        return all_items
    
    def _resize(self):
        """Resize hash table when load factor gets too high."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        
        # Rehash all existing items
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def load_factor(self):
        """Return current load factor."""
        return self.size / self.capacity
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        items = self.items()
        return "{" + ", ".join([f"'{k}': {v}" for k, v in items]) + "}"


class LinearProbingHashTable:
    """Hash table implementation using linear probing for collision resolution."""
    
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.deleted = [False] * self.capacity  # Track deleted slots
    
    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """Insert or update key-value pair using linear probing."""
        if self.size >= self.capacity * 0.75:
            self._resize()
        
        index = self._hash(key)
        
        # Linear probing to find empty slot or existing key
        while self.keys[index] is not None and not self.deleted[index]:
            if self.keys[index] == key:
                self.values[index] = value  # Update existing
                return
            index = (index + 1) % self.capacity
        
        # Found empty slot or deleted slot
        if self.keys[index] is None or self.deleted[index]:
            self.keys[index] = key
            self.values[index] = value
            self.deleted[index] = False
            self.size += 1
    
    def get(self, key):
        """Get value for given key using linear probing."""
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                return self.values[index]
            index = (index + 1) % self.capacity
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair using lazy deletion."""
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                self.deleted[index] = True
                self.size -= 1
                return self.values[index]
            index = (index + 1) % self.capacity
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Check if key exists."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def _resize(self):
        """Resize and rehash when load factor gets too high."""
        old_keys = self.keys
        old_values = self.values
        old_deleted = self.deleted
        
        self.capacity *= 2
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.deleted = [False] * self.capacity
        
        # Rehash all non-deleted items
        for i in range(len(old_keys)):
            if old_keys[i] is not None and not old_deleted[i]:
                self.put(old_keys[i], old_values[i])
    
    def __len__(self):
        return self.size


def first_non_repeating_char(s):
    """
    Find first non-repeating character in string using hash table.
    Returns the character or None if all characters repeat.
    """
    char_count = {}
    
    # Count frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None


def group_anagrams(words):
    """
    Group anagrams together using hash table.
    Returns list of lists where each inner list contains anagrams.
    """
    anagram_groups = {}
    
    for word in words:
        # Sort characters to create key for anagrams
        sorted_word = ''.join(sorted(word.lower()))
        
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())


def two_sum_hash(nums, target):
    """
    Find two numbers that sum to target using hash table.
    Returns indices of the two numbers.
    Time Complexity: O(n)
    """
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return None


def find_duplicate_hash(nums):
    """
    Find first duplicate in array using hash table.
    Returns the duplicate number or None if no duplicates.
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    
    return None


def longest_substring_without_repeating(s):
    """
    Find length of longest substring without repeating characters.
    Uses sliding window with hash table.
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


# Example usage and demonstrations
if __name__ == "__main__":
    # Hash Table with Separate Chaining example
    print("=== Hash Table (Separate Chaining) Example ===")
    ht = HashTable()
    
    # Insert some key-value pairs
    ht.put("name", "Alice")
    ht.put("age", 30)
    ht.put("city", "New York")
    ht.put("country", "USA")
    
    print(f"Hash table: {ht}")
    print(f"Size: {len(ht)}")
    print(f"Load factor: {ht.load_factor():.2f}")
    
    print(f"Get 'name': {ht.get('name')}")
    print(f"Contains 'age': {ht.contains('age')}")
    
    # Test resizing
    for i in range(10):
        ht.put(f"key{i}", f"value{i}")
    
    print(f"After adding 10 more items - Size: {len(ht)}, Load factor: {ht.load_factor():.2f}")
    
    # Linear Probing Hash Table example
    print("\n=== Hash Table (Linear Probing) Example ===")
    lp_ht = LinearProbingHashTable()
    
    for i in range(5):
        lp_ht.put(f"key{i}", i * 10)
    
    print(f"Linear probing hash table size: {len(lp_ht)}")
    print(f"Get 'key2': {lp_ht.get('key2')}")
    
    # First non-repeating character example
    print("\n=== First Non-Repeating Character ===")
    test_strings = ["abccba", "abcabc", "abcdef"]
    for s in test_strings:
        result = first_non_repeating_char(s)
        print(f"'{s}' -> First non-repeating: {result}")
    
    # Group anagrams example
    print("\n=== Group Anagrams ===")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram_groups = group_anagrams(words)
    print(f"Words: {words}")
    print(f"Anagram groups: {anagram_groups}")
    
    # Two sum with hash table example
    print("\n=== Two Sum (Hash Table) ===")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum_hash(nums, target)
    print(f"Array: {nums}, Target: {target}")
    print(f"Indices: {result}")
    
    # Longest substring without repeating characters
    print("\n=== Longest Substring Without Repeating ===")
    test_strings = ["abcabcbb", "bbbbb", "pwwkew", ""]
    for s in test_strings:
        length = longest_substring_without_repeating(s)
        print(f"'{s}' -> Length: {length}")