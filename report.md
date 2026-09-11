# Programming Assignment 4: Binary Search Tree Implementation and AVL Analysis

**Name:** Erica Cepeda

## 1. Explanation of Binary Search Trees

Values in a binary search tree are ordered according to the ordering property. A node may have a left child and/or right child. Values less than the current node go into its left subtree; values greater than the node are placed in its right subtree. Duplicate values are not inserted in this implementation.

Insertion starts from the root and compares the new value to nodes along the way. The algorithm goes to the left if the value is smaller than the current node and right otherwise. It continues to move this way until reaching an empty position. Searching is similar to insertion except that it stops when either target value or an empty position is reached.

In-order traversal goes from left subtree to the current node and then to the right subtree. By virtue of the binary search tree ordering property, in-order traversal returns values in ascending order.

## 2. Explanation of Implemented Operations

The `insert` method recursively finds an appropriate place for insertion and creates a node there. The `search` operation goes left or right depending on how the target value compares with the current node.

The `delete` method deals with three different cases. A leaf node can be deleted immediately. A node with only one child is replaced with its child. If a node has two children, it is replaced by the in-order successor, which is the minimum value in the right subtree of the node. The successor is deleted from its original place afterwards.

The `in_order_traversal` operation returns values in ascending order by visiting nodes in left-root-right order. The additional `pre_order_traversal` operation visits nodes in root-left-right order and helps demonstrate the shape of the tree.

## 3. Runtime Analysis

Runtime of operations in a binary search tree depends on the tree height `h`. Each of the operations (`search`, `insertion`, and `deletion`) has `O(h)` complexity since they traverse one path through the tree starting from the root.

| Operation | Average Case | Worst Case |
|---|---:|---:|
| Search | O(log n) | O(n) |
| Insertion | O(log n) | O(n) |
| Deletion | O(log n) | O(n) |

As long as the tree is reasonably balanced, its height increases proportionally to `log n`. Hence, search, insertion, and deletion operations take `O(log n)` time on average. During the balanced test, values `[50, 30, 70, 20, 40, 60, 80]` were inserted. This caused the tree to be built with values on both sides of the root, thus creating a tree of relatively small height.

During the sorted-insertion test, values are inserted into the tree in increasing order. As a result, each new value becomes the right child of the previous value. For example, values `[10, 20, 30, 40, 50]` resulted in the right-skewed tree. Pre-order traversal of this tree is the same as the order of insertion, indicating that the tree behaves like a linked list rather than a balanced tree. As a consequence, the tree’s height grows linearly with the number of nodes, causing worst-case `O(n)` performance of search, insertion, and deletion.

## 4. AVL Balance Factor and Rotations

AVL tree is a self-balancing binary search tree. The aim of the balance factor is to find the difference between heights of the left and right subtree of the node. It can be computed using the formula:

`balance factor = height of left subtree - height of right subtree`

If a node’s balance factor equals `-1`, `0`, or `1`, the node is balanced; if not, then it is unbalanced. Rotations help AVL trees maintain their balance and keep their height at `O(log n)` level.

A single rotation fixes the situation if the imbalance follows one direction, namely, left-left or right-right. Double rotation is required if the new value changes the direction, for example, left-right or right-left.

| Case | Description | Rotation Needed |
|---|---|---|
| LL | Insertion occurs in the left subtree of the left child | Single right rotation |
| RR | Insertion occurs in the right subtree of the right child | Single left rotation |
| LR | Insertion occurs in the right subtree of the left child | Left rotation on the left child, followed by a right rotation |
| RL | Insertion occurs in the left subtree of the right child | Right rotation on the right child, followed by a left rotation |

The sorted-insertion test shows why the AVL balancing is useful. Since a binary search tree does not rebalance itself automatically, the sorted values `[10, 20, 30, 40, 50]` resulted in the right-skewed tree. AVL tree, however, would be able to detect imbalance and use rotations to decrease the tree’s height and thus maintain `O(log n)` runtime of its main operations.

## 5. Test Results

All required and additional test cases were passed successfully. Balanced insertion resulted in in-order traversal `[20, 30, 40, 50, 60, 70, 80]`. Sorted-insertion gave the same result for in-order and pre-order traversals, proving the right-skewed structure of the tree.

Search gave `True` for an existing value `60` and `False` for non-existing value `90`. Deletion test was successful in deleting leaf node `20`, node `80` with only one child, and node `70` with two children. In-order traversal after each deletion confirmed that all the other values were still sorted.

The additional application test inserted ACC computer science course numbers `[2325, 1336, 4302, 1301, 2346]`. In-order traversal returned `[1301, 1336, 2325, 2346, 4302]`. The program found course `2325` and determined that course `9999` was non-existent.

![Binary search tree Tests 1–4](01_bst_tests.png)

![Binary search tree Tests 5–7](02_bst_tests.png)

## 6. Reflection

Through this assignment, I learned that the efficiency of a binary search tree depends not only on the code implementation of its operations. The order of insertion has great influence on the shape and height of the tree. Thus, when inserting values around the root, I got a relatively balanced tree which allowed search operations to eliminate most of the remaining values after each comparison. In the opposite case of inserting sorted values, I obtained a right-skewed structure that behaved like a linked list and required more steps to reach deeper values.

Implementation of three types of deletions also helped me see that deletion is a much more complicated operation than insertion and searching. Deleting a leaf node was quite simple, but to delete a node with two children, it was necessary to find the in-order successor while preserving the ordering property. AVL analysis gave me insight into solving this problem. Rotations do not simply modify the tree structure but prevent the tree from losing its efficiency in terms of performance. Lastly, the ACC course-number test connected binary search trees with practical record retrieval problem.
