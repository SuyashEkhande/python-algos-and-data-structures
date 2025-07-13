"""
Tree Problems

This module contains solutions to common tree-related coding interview problems
from platforms like LeetCode, HackerRank, etc.
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


def inorder_traversal(root):
    """
    LeetCode #94: Binary Tree Inorder Traversal
    Return inorder traversal of binary tree.
    
    Time: O(n), Space: O(n)
    """
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result


def inorder_traversal_iterative(root):
    """
    Iterative version of inorder traversal using stack.
    """
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result


def level_order_traversal(root):
    """
    LeetCode #102: Binary Tree Level Order Traversal
    Return level order traversal as list of lists.
    
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result


def max_depth(root):
    """
    LeetCode #104: Maximum Depth of Binary Tree
    Find maximum depth of binary tree.
    
    Time: O(n), Space: O(h) where h is height
    """
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_same_tree(p, q):
    """
    LeetCode #100: Same Tree
    Check if two binary trees are identical.
    
    Time: O(n), Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


def is_symmetric(root):
    """
    LeetCode #101: Symmetric Tree
    Check if binary tree is symmetric around its center.
    
    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root) if root else True


def has_path_sum(root, targetSum):
    """
    LeetCode #112: Path Sum
    Check if tree has root-to-leaf path with given sum.
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == targetSum
    
    remaining = targetSum - root.val
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))


def path_sum_ii(root, targetSum):
    """
    LeetCode #113: Path Sum II
    Find all root-to-leaf paths with given sum.
    
    Time: O(n²), Space: O(n)
    """
    result = []
    
    def dfs(node, remaining, path):
        if not node:
            return
        
        path.append(node.val)
        
        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])  # Make copy of path
        else:
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)
        
        path.pop()  # Backtrack
    
    dfs(root, targetSum, [])
    return result


def invert_tree(root):
    """
    LeetCode #226: Invert Binary Tree
    Invert (mirror) the binary tree.
    
    Time: O(n), Space: O(h)
    """
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


def lowest_common_ancestor(root, p, q):
    """
    LeetCode #236: Lowest Common Ancestor of Binary Tree
    Find LCA of two nodes in binary tree.
    
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right


def diameter_of_tree(root):
    """
    LeetCode #543: Diameter of Binary Tree
    Find diameter (longest path between any two nodes).
    
    Time: O(n), Space: O(h)
    """
    max_diameter = [0]
    
    def depth(node):
        if not node:
            return 0
        
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        
        # Update diameter
        max_diameter[0] = max(max_diameter[0], left_depth + right_depth)
        
        return 1 + max(left_depth, right_depth)
    
    depth(root)
    return max_diameter[0]


def is_valid_bst(root):
    """
    LeetCode #98: Validate Binary Search Tree
    Check if tree is valid BST.
    
    Time: O(n), Space: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def kth_smallest_in_bst(root, k):
    """
    LeetCode #230: Kth Smallest Element in BST
    Find kth smallest element in BST.
    
    Time: O(h + k), Space: O(h)
    """
    stack = []
    current = root
    
    while True:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        k -= 1
        
        if k == 0:
            return current.val
        
        current = current.right


def serialize_tree(root):
    """
    LeetCode #297: Serialize and Deserialize Binary Tree
    Serialize tree to string.
    
    Time: O(n), Space: O(n)
    """
    def preorder(node):
        if not node:
            return "null,"
        
        return str(node.val) + "," + preorder(node.left) + preorder(node.right)
    
    return preorder(root)


def deserialize_tree(data):
    """
    Deserialize string to tree.
    """
    def build_tree():
        val = next(values)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = build_tree()
        node.right = build_tree()
        return node
    
    values = iter(data.split(","))
    return build_tree()


def build_tree_from_preorder_inorder(preorder, inorder):
    """
    LeetCode #105: Construct Binary Tree from Preorder and Inorder
    Build tree from preorder and inorder traversals.
    
    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = build_tree_from_preorder_inorder(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_from_preorder_inorder(preorder[mid+1:], inorder[mid+1:])
    
    return root


def binary_tree_right_side_view(root):
    """
    LeetCode #199: Binary Tree Right Side View
    Return values visible from right side.
    
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            
            # Last node in level is visible from right
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result


def sum_root_to_leaf_numbers(root):
    """
    LeetCode #129: Sum Root to Leaf Numbers
    Sum all root-to-leaf numbers.
    
    Time: O(n), Space: O(h)
    """
    def dfs(node, current_number):
        if not node:
            return 0
        
        current_number = current_number * 10 + node.val
        
        if not node.left and not node.right:
            return current_number
        
        return dfs(node.left, current_number) + dfs(node.right, current_number)
    
    return dfs(root, 0)


def flatten_tree_to_linked_list(root):
    """
    LeetCode #114: Flatten Binary Tree to Linked List
    Flatten tree to linked list in-place.
    
    Time: O(n), Space: O(1)
    """
    current = root
    
    while current:
        if current.left:
            # Find rightmost node in left subtree
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right
            
            # Connect right subtree to rightmost
            rightmost.right = current.right
            current.right = current.left
            current.left = None
        
        current = current.right


def count_good_nodes(root):
    """
    LeetCode #1448: Count Good Nodes in Binary Tree
    Count nodes where path from root has no greater values.
    
    Time: O(n), Space: O(h)
    """
    def dfs(node, max_val):
        if not node:
            return 0
        
        count = 1 if node.val >= max_val else 0
        new_max = max(max_val, node.val)
        
        count += dfs(node.left, new_max) + dfs(node.right, new_max)
        return count
    
    return dfs(root, float('-inf'))


# Helper function to create a sample tree for testing
def create_sample_tree():
    """
    Create a sample tree:
        3
       / \
      9   20
         /  \
        15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


# Example usage and test cases
if __name__ == "__main__":
    print("=== Tree Problems Solutions ===")
    
    # Create sample tree
    root = create_sample_tree()
    
    # Inorder Traversal
    print("\n1. Inorder Traversal:")
    result = inorder_traversal(root)
    print(f"Inorder (recursive): {result}")
    result = inorder_traversal_iterative(root)
    print(f"Inorder (iterative): {result}")
    
    # Level Order Traversal
    print("\n2. Level Order Traversal:")
    result = level_order_traversal(root)
    print(f"Level order: {result}")
    
    # Maximum Depth
    print("\n3. Maximum Depth:")
    result = max_depth(root)
    print(f"Maximum depth: {result}")
    
    # Symmetric Tree
    print("\n4. Symmetric Tree:")
    result = is_symmetric(root)
    print(f"Is symmetric: {result}")
    
    # Path Sum
    print("\n5. Path Sum:")
    target = 38  # 3 + 20 + 15
    result = has_path_sum(root, target)
    print(f"Has path sum {target}: {result}")
    
    # Path Sum II
    result = path_sum_ii(root, target)
    print(f"All paths with sum {target}: {result}")
    
    # Diameter
    print("\n6. Diameter of Tree:")
    result = diameter_of_tree(root)
    print(f"Diameter: {result}")
    
    # Create BST for validation
    bst = TreeNode(5)
    bst.left = TreeNode(3)
    bst.right = TreeNode(8)
    bst.left.left = TreeNode(1)
    bst.left.right = TreeNode(4)
    
    # Validate BST
    print("\n7. Validate BST:")
    result = is_valid_bst(bst)
    print(f"Is valid BST: {result}")
    
    # Kth smallest in BST
    print("\n8. Kth Smallest in BST:")
    k = 3
    result = kth_smallest_in_bst(bst, k)
    print(f"{k}th smallest element: {result}")
    
    # Serialize and Deserialize
    print("\n9. Serialize Tree:")
    serialized = serialize_tree(root)
    print(f"Serialized: {serialized}")
    
    # Right Side View
    print("\n10. Right Side View:")
    result = binary_tree_right_side_view(root)
    print(f"Right side view: {result}")
    
    # Sum Root to Leaf Numbers
    print("\n11. Sum Root to Leaf Numbers:")
    result = sum_root_to_leaf_numbers(root)
    print(f"Sum of root-to-leaf numbers: {result}")
    
    # Count Good Nodes
    print("\n12. Count Good Nodes:")
    result = count_good_nodes(root)
    print(f"Number of good nodes: {result}")
    
    print(f"\nNote: These are fundamental tree problems covering:")
    print("- Tree traversals (inorder, level-order)")
    print("- Tree properties (depth, diameter, symmetry)")
    print("- Path problems (path sum, root-to-leaf)")
    print("- BST operations (validation, kth smallest)")
    print("- Tree construction and serialization")