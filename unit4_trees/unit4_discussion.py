"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the value for this node
        self.value = value

        # New nodes start without a left or right child
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Start with an empty tree
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The recursive helper finds the correct place for the value.
        # Smaller values go left, while larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If there is no node here, create a new one
        if node is None:
            return Node(value)

        # Smaller values are inserted into the left subtre
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values are inserted into the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the node after the insertion is complete
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Start searching from the root of the tree.
        # A BST can reduce the search space because each comparison
        # tells us whether to continue left or right instead of
        # checking every value one by one.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If there is no node here, the value was not found
        if node is None:
            return False

        # If the current node matches the value, it was found
        if value == node.value:
            return True

        # Search the left side if the value is smaller
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Otherwise, search the right side
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Create an empty list to store the values
        values = []

        # Start the in-order traversal from the root
        self._inorder_recursive(self.root, values)

        # Return the completed list
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Only continue if the current node exists
        if node is not None:
            # Visit the left subtree first
            self._inorder_recursive(node.left, values)

            # Add the current node's value to the list
            values.append(node.value)

            # Visit the right subtree last
            self._inorder_recursive(node.right, values)

            # This produces sorted output because smaller values are
            # stored on the left and larger values are stored on the right.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create a new Binary Search Tree
    tree = BST()

    # Insert values into the tree. The values will create
    # both left and right subtrees.
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    # Display the values that were inserted
    print("Values inserted:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits the left subtree, the current node,
    # and then the right subtree, which display BST values in sorted order.
    print("In-order traversal:", tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Search for two values that exist in the tree
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # Search for two values that do not exist in the tree
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Create an empty BST to test what happens when it has no nodes
    empty_tree = BST()

    # Searching an empty tree returns False because there are no values to search
    print("Search empty tree for 50:", empty_tree.search(50))

    # An in-order traversal of an empty tree returns an empty list
    print("Empty tree traversal:", empty_tree.inorder())



if __name__ == "__main__":
    main()