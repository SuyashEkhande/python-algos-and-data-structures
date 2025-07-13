"""
Stack and Queue Data Structure Implementations

This module contains various stack and queue implementations with common operations.
"""


class Stack:
    """Stack implementation using list."""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item from stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in stack."""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"


class Queue:
    """Queue implementation using list."""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item from queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def rear(self):
        """Return rear item without removing it."""
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self.items[-1]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in queue."""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({self.items})"


class CircularQueue:
    """Circular Queue implementation using fixed-size array."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def enqueue(self, item):
        """Add item to circular queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.count += 1
    
    def dequeue(self):
        """Remove and return item from front of circular queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item
    
    def peek_front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[self.front]
    
    def is_empty(self):
        """Check if queue is empty."""
        return self.count == 0
    
    def is_full(self):
        """Check if queue is full."""
        return self.count == self.capacity
    
    def size(self):
        """Return number of items in queue."""
        return self.count
    
    def __str__(self):
        if self.is_empty():
            return "CircularQueue([])"
        
        result = []
        index = self.front
        for _ in range(self.count):
            result.append(self.items[index])
            index = (index + 1) % self.capacity
        
        return f"CircularQueue({result})"


class Deque:
    """Double-ended queue implementation."""
    
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        """Add item to front of deque."""
        self.items.insert(0, item)
    
    def add_rear(self, item):
        """Add item to rear of deque."""
        self.items.append(item)
    
    def remove_front(self):
        """Remove and return item from front of deque."""
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop(0)
    
    def remove_rear(self):
        """Remove and return item from rear of deque."""
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop()
    
    def peek_front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.items[0]
    
    def peek_rear(self):
        """Return rear item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self.items[-1]
    
    def is_empty(self):
        """Check if deque is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in deque."""
        return len(self.items)
    
    def __str__(self):
        return f"Deque({self.items})"


def is_balanced_parentheses(expression):
    """
    Check if parentheses in expression are balanced using stack.
    Supports (), [], and {} brackets.
    """
    stack = Stack()
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            
            last_opening = stack.pop()
            if pairs[last_opening] != char:
                return False
    
    return stack.is_empty()


def postfix_evaluation(expression):
    """
    Evaluate postfix expression using stack.
    Example: "3 4 + 2 *" = (3 + 4) * 2 = 14
    """
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            
            stack.push(result)
        else:
            try:
                stack.push(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


def infix_to_postfix(expression):
    """
    Convert infix expression to postfix using stack.
    Example: "3 + 4 * 2" -> "3 4 2 * +"
    """
    stack = Stack()
    postfix = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    tokens = expression.split()
    
    for token in tokens:
        if token.isalnum():
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        elif token in precedence:
            while (not stack.is_empty() and 
                   stack.peek() != '(' and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                postfix.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ' '.join(postfix)


# Example usage and demonstrations
if __name__ == "__main__":
    # Stack example
    print("=== Stack Example ===")
    stack = Stack()
    for i in [1, 2, 3, 4, 5]:
        stack.push(i)
    print(f"Stack after pushing 1-5: {stack}")
    
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    
    # Queue example
    print("\n=== Queue Example ===")
    queue = Queue()
    for i in [10, 20, 30, 40]:
        queue.enqueue(i)
    print(f"Queue after enqueuing 10,20,30,40: {queue}")
    
    print(f"Front: {queue.front()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue}")
    
    # Circular Queue example
    print("\n=== Circular Queue Example ===")
    cq = CircularQueue(5)
    for i in [1, 2, 3, 4, 5]:
        cq.enqueue(i)
    print(f"Circular queue after filling: {cq}")
    
    print(f"Dequeue: {cq.dequeue()}")
    print(f"Dequeue: {cq.dequeue()}")
    cq.enqueue(6)
    cq.enqueue(7)
    print(f"After dequeuing 2 and enqueuing 6,7: {cq}")
    
    # Balanced parentheses example
    print("\n=== Balanced Parentheses Example ===")
    expressions = ["()", "()[]{}", "([{}])", "(()", "([)]"]
    for expr in expressions:
        result = is_balanced_parentheses(expr)
        print(f"'{expr}' is balanced: {result}")
    
    # Postfix evaluation example
    print("\n=== Postfix Evaluation Example ===")
    postfix_expr = "3 4 + 2 *"
    result = postfix_evaluation(postfix_expr)
    print(f"'{postfix_expr}' = {result}")
    
    # Infix to postfix conversion example
    print("\n=== Infix to Postfix Conversion ===")
    infix_expr = "3 + 4 * 2"
    postfix_result = infix_to_postfix(infix_expr)
    print(f"Infix: '{infix_expr}' -> Postfix: '{postfix_result}'")