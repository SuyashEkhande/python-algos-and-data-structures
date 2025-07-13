"""
Linked List Data Structure Implementation

This module contains various linked list implementations and operations.
"""


class ListNode:
    """Node class for linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)


class SinglyLinkedList:
    """Singly Linked List implementation."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """Add element to the end of the list."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, val):
        """Add element to the beginning of the list."""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, val):
        """Insert element at given index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, val):
        """Delete first occurrence of value."""
        if not self.head:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, val):
        """Find index of value in list."""
        current = self.head
        index = 0
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
        return -1
    
    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
    
    def to_list(self):
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return " -> ".join(map(str, self.to_list())) + " -> None"


class DoublyListNode:
    """Node class for doubly linked list."""
    
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """Doubly Linked List implementation."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, val):
        """Add element to the end of the list."""
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def prepend(self, val):
        """Add element to the beginning of the list."""
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, val):
        """Delete first occurrence of value."""
        current = self.head
        
        while current:
            if current.val == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def to_list(self):
        """Convert doubly linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return " <-> ".join(map(str, self.to_list()))


def detect_cycle(head):
    """
    Detect if linked list has a cycle using Floyd's cycle detection.
    Returns True if cycle exists, False otherwise.
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted linked lists.
    Returns head of merged list.
    """
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = list1 or list2
    
    return dummy.next


def find_middle(head):
    """
    Find middle node of linked list using two-pointer technique.
    For even length, returns the second middle node.
    """
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# Example usage and demonstrations
if __name__ == "__main__":
    # Singly Linked List example
    print("=== Singly Linked List Example ===")
    sll = SinglyLinkedList()
    for i in [1, 2, 3, 4, 5]:
        sll.append(i)
    print(f"Original list: {sll}")
    
    sll.insert(2, 2.5)
    print(f"After inserting 2.5 at index 2: {sll}")
    
    sll.delete(3)
    print(f"After deleting 3: {sll}")
    
    print(f"Index of 4: {sll.find(4)}")
    
    sll.reverse()
    print(f"After reversing: {sll}")
    
    # Doubly Linked List example
    print("\n=== Doubly Linked List Example ===")
    dll = DoublyLinkedList()
    for i in [10, 20, 30, 40]:
        dll.append(i)
    print(f"Doubly linked list: {dll}")
    
    dll.prepend(5)
    print(f"After prepending 5: {dll}")
    
    dll.delete(20)
    print(f"After deleting 20: {dll}")
    
    # Merge sorted lists example
    print("\n=== Merge Sorted Lists Example ===")
    # Create first sorted list: 1 -> 2 -> 4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    # Create second sorted list: 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    merged = merge_sorted_lists(list1, list2)
    
    # Convert to list for display
    merged_list = []
    current = merged
    while current:
        merged_list.append(current.val)
        current = current.next
    
    print(f"Merged sorted lists: {merged_list}")