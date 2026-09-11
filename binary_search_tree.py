"""Binary search tree implementation and test cases."""


class Node:
    """Represents one node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Implements a binary search tree and its major operations."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the binary search tree."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            print(f"Value {value} already exists and was not inserted.")

        return node

    def search(self, value):
        """Return True if a value exists in the tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def delete(self, value):
        """Delete a value from the binary search tree."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: The node is a leaf.
            if node.left is None and node.right is None:
                return None

            # Case 2: The node has only a right child.
            if node.left is None:
                return node.right

            # Case 2: The node has only a left child.
            if node.right is None:
                return node.left

            # Case 3: The node has two children.
            successor = self._find_minimum(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(
                node.right, successor.value
            )

        return node

    def _find_minimum(self, node):
        """Find the node containing the smallest value in a subtree."""
        current = node

        while current.left is not None:
            current = current.left

        return current

    def in_order_traversal(self):
        """Return the tree values in ascending order."""
        values = []
        self._in_order_recursive(self.root, values)
        return values

    def _in_order_recursive(self, node, values):
        if node is not None:
            self._in_order_recursive(node.left, values)
            values.append(node.value)
            self._in_order_recursive(node.right, values)

    def pre_order_traversal(self):
        """Return tree values in root-left-right order."""
        values = []
        self._pre_order_recursive(self.root, values)
        return values

    def _pre_order_recursive(self, node, values):
        if node is not None:
            values.append(node.value)
            self._pre_order_recursive(node.left, values)
            self._pre_order_recursive(node.right, values)


def print_test_result(test_name, passed):
    """Print a clear PASS or FAIL result."""
    status = "PASS" if passed else "FAIL"
    print(f"{test_name}: {status}")


def run_tests():
    """Run the required and additional test cases."""

    print("=" * 60)
    print("BINARY SEARCH TREE TESTS")
    print("=" * 60)

    # Test 1: Insert values that create a reasonably balanced tree.
    print("\nTEST 1: REASONABLY BALANCED TREE")

    balanced_tree = BinarySearchTree()
    balanced_values = [50, 30, 70, 20, 40, 60, 80]

    for value in balanced_values:
        balanced_tree.insert(value)

    print("Inserted values:", balanced_values)
    print("In-order traversal:", balanced_tree.in_order_traversal())
    print("Pre-order traversal:", balanced_tree.pre_order_traversal())

    print_test_result(
        "Balanced-tree insertion",
        balanced_tree.in_order_traversal() == sorted(balanced_values),
    )

    # Test 2: Insert values in sorted order.
    print("\nTEST 2: SORTED INSERTION")

    sorted_tree = BinarySearchTree()
    sorted_values = [10, 20, 30, 40, 50]

    for value in sorted_values:
        sorted_tree.insert(value)

    print("Inserted values:", sorted_values)
    print("In-order traversal:", sorted_tree.in_order_traversal())
    print("Pre-order traversal:", sorted_tree.pre_order_traversal())
    print("The pre-order output matches the insertion order.")
    print("This demonstrates that the tree is skewed to the right.")

    print_test_result(
        "Sorted insertion",
        sorted_tree.in_order_traversal() == sorted_values,
    )

    # Test 3: Search for existing and missing values.
    print("\nTEST 3: SEARCH")

    existing_value = 60
    missing_value = 90

    print(
        f"Search for existing value {existing_value}:",
        balanced_tree.search(existing_value),
    )
    print(
        f"Search for missing value {missing_value}:",
        balanced_tree.search(missing_value),
    )

    print_test_result(
        "Existing-value search",
        balanced_tree.search(existing_value) is True,
    )
    print_test_result(
        "Missing-value search",
        balanced_tree.search(missing_value) is False,
    )

    # Test 4: Delete a leaf node.
    print("\nTEST 4: DELETE A LEAF NODE")

    leaf_tree = BinarySearchTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        leaf_tree.insert(value)

    print("Before deleting leaf node 20:")
    print(leaf_tree.in_order_traversal())

    leaf_tree.delete(20)

    print("After deleting leaf node 20:")
    print(leaf_tree.in_order_traversal())

    print_test_result(
        "Leaf-node deletion",
        leaf_tree.in_order_traversal()
        == [30, 40, 50, 60, 70, 80],
    )

    # Test 5: Delete a node with one child.
    print("\nTEST 5: DELETE A NODE WITH ONE CHILD")

    one_child_tree = BinarySearchTree()

    for value in [50, 30, 70, 60, 80, 75]:
        one_child_tree.insert(value)

    print("Before deleting node 80, which has child 75:")
    print(one_child_tree.in_order_traversal())

    one_child_tree.delete(80)

    print("After deleting node 80:")
    print(one_child_tree.in_order_traversal())

    print_test_result(
        "One-child deletion",
        one_child_tree.in_order_traversal()
        == [30, 50, 60, 70, 75],
    )

    # Test 6: Delete a node with two children.
    print("\nTEST 6: DELETE A NODE WITH TWO CHILDREN")

    two_child_tree = BinarySearchTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        two_child_tree.insert(value)

    print("Before deleting node 70, which has children 60 and 80:")
    print(two_child_tree.in_order_traversal())

    two_child_tree.delete(70)

    print("After deleting node 70:")
    print(two_child_tree.in_order_traversal())

    print_test_result(
        "Two-child deletion",
        two_child_tree.in_order_traversal()
        == [20, 30, 40, 50, 60, 80],
    )

    # Test 7: Additional real-world application.
    print("\nTEST 7: ACC COMPUTER SCIENCE COURSE NUMBERS")
    print("This test models organizing ACC course numbers.")

    course_tree = BinarySearchTree()
    course_numbers = [2325, 1336, 4302, 1301, 2346]

    for course_number in course_numbers:
        course_tree.insert(course_number)

    print("Course numbers entered:", course_numbers)
    print(
        "Course numbers in sorted order:",
        course_tree.in_order_traversal(),
    )
    print("Search for COSC 2325:", course_tree.search(2325))
    print("Search for course 9999:", course_tree.search(9999))

    print_test_result(
        "Course-number insertion",
        course_tree.in_order_traversal()
        == [1301, 1336, 2325, 2346, 4302],
    )
    print_test_result(
        "Course-number search",
        course_tree.search(2325) is True
        and course_tree.search(9999) is False,
    )

    print("\n" + "=" * 60)
    print("ALL REQUIRED AND ADDITIONAL TESTS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
