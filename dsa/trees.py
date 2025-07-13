"""
Tree Data Structure Implementations

This module contains various tree implementations including Binary Tree, Binary Search Tree, and AVL Tree.
"""


class TreeNode:
    """Node class for binary tree."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


class BinaryTree:
    """Binary Tree implementation with common operations."""
    
    def __init__(self, root=None):
        self.root = root
    
    def inorder_traversal(self, node=None):
        """Inorder traversal: Left -> Root -> Right"""
        if node is None:
            node = self.root
        
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.val)
            self._inorder_helper(node.right, result)
    
    def preorder_traversal(self, node=None):
        """Preorder traversal: Root -> Left -> Right"""
        if node is None:
            node = self.root
        
        result = []
        self._preorder_helper(node, result)
        return result
    
    def _preorder_helper(self, node, result):
        """Helper method for preorder traversal."""
        if node:
            result.append(node.val)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)
    
    def postorder_traversal(self, node=None):
        """Postorder traversal: Left -> Right -> Root"""
        if node is None:
            node = self.root
        
        result = []
        self._postorder_helper(node, result)
        return result
    
    def _postorder_helper(self, node, result):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.val)
    
    def level_order_traversal(self):
        """Level order traversal (BFS) using queue."""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """Calculate height of tree."""
        if node is None:
            node = self.root
        
        return self._height_helper(node)
    
    def _height_helper(self, node):
        """Helper method for calculating height."""
        if not node:
            return -1
        
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        
        return 1 + max(left_height, right_height)
    
    def size(self, node=None):
        """Calculate number of nodes in tree."""
        if node is None:
            node = self.root
        
        return self._size_helper(node)
    
    def _size_helper(self, node):
        """Helper method for calculating size."""
        if not node:
            return 0
        
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)


class BinarySearchTree:
    """Binary Search Tree implementation."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert value into BST."""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        """Helper method for recursive insertion."""
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        # Ignore duplicates
        
        return node
    
    def search(self, val):
        """Search for value in BST."""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        """Helper method for recursive search."""
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def delete(self, val):
        """Delete value from BST."""
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        """Helper method for recursive deletion."""
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node has two children
            min_node = self._find_min(node.right)
            node.val = min_node.val
            node.right = self._delete_recursive(node.right, min_node.val)
        
        return node
    
    def _find_min(self, node):
        """Find minimum value node in subtree."""
        while node.left:
            node = node.left
        return node
    
    def _find_max(self, node):
        """Find maximum value node in subtree."""
        while node.right:
            node = node.right
        return node
    
    def inorder_traversal(self):
        """Inorder traversal of BST (gives sorted order)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def is_valid_bst(self):
        """Check if tree is a valid BST."""
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """Helper for BST validation."""
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.val) and
                self._is_valid_bst_recursive(node.right, node.val, max_val))


class AVLNode:
    """Node class for AVL tree with height information."""
    
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """AVL Tree (self-balancing BST) implementation."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert value into AVL tree."""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        """Helper method for recursive insertion with balancing."""
        # Step 1: Perform normal BST insertion
        if not node:
            return AVLNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        else:
            return node  # Duplicate values not allowed
        
        # Step 2: Update height of current node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: If unbalanced, perform rotations
        # Left Left Case
        if balance > 1 and val < node.left.val:
            return self._right_rotate(node)
        
        # Right Right Case
        if balance < -1 and val > node.right.val:
            return self._left_rotate(node)
        
        # Left Right Case
        if balance > 1 and val > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Right Left Case
        if balance < -1 and val < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _get_height(self, node):
        """Get height of node."""
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Get balance factor of node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _left_rotate(self, z):
        """Perform left rotation."""
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def _right_rotate(self, z):
        """Perform right rotation."""
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def inorder_traversal(self):
        """Inorder traversal of AVL tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)


def lowest_common_ancestor(root, p, q):
    """
    Find lowest common ancestor of two nodes in BST.
    """
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root


def is_symmetric(root):
    """
    Check if binary tree is symmetric.
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    return is_mirror(root.left, root.right)


def max_depth(root):
    """
    Find maximum depth of binary tree.
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Example usage and demonstrations
if __name__ == "__main__":
    # Binary Tree example
    print("=== Binary Tree Example ===")
    # Create tree:     1
    #                 / \
    #                2   3
    #               / \
    #              4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    bt = BinaryTree(root)
    print(f"Inorder: {bt.inorder_traversal()}")
    print(f"Preorder: {bt.preorder_traversal()}")
    print(f"Postorder: {bt.postorder_traversal()}")
    print(f"Level order: {bt.level_order_traversal()}")
    print(f"Height: {bt.height()}")
    print(f"Size: {bt.size()}")
    
    # Binary Search Tree example
    print("\n=== Binary Search Tree Example ===")
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    print(f"Inserted values: {values}")
    print(f"Inorder traversal (sorted): {bst.inorder_traversal()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    search_val = 40
    found = bst.search(search_val)
    print(f"Search for {search_val}: {'Found' if found else 'Not found'}")
    
    bst.delete(30)
    print(f"After deleting 30: {bst.inorder_traversal()}")
    
    # AVL Tree example
    print("\n=== AVL Tree Example ===")
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    
    for val in values:
        avl.insert(val)
    
    print(f"Inserted values: {values}")
    print(f"AVL tree inorder: {avl.inorder_traversal()}")
    
    # Tree properties example
    print("\n=== Tree Properties Example ===")
    print(f"Maximum depth: {max_depth(root)}")
    print(f"Is symmetric: {is_symmetric(root)}")
    
    # Create symmetric tree for testing
    sym_root = TreeNode(1)
    sym_root.left = TreeNode(2)
    sym_root.right = TreeNode(2)
    sym_root.left.left = TreeNode(3)
    sym_root.left.right = TreeNode(4)
    sym_root.right.left = TreeNode(4)
    sym_root.right.right = TreeNode(3)
    
    print(f"Symmetric tree is symmetric: {is_symmetric(sym_root)}")