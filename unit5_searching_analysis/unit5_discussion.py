"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Check each value in the list one at a time
    for i in range(len(lst)):
        # Return the index if the target is found
        if lst[i] == target:
            return i

    # Return -1 if the target is not found
    # Linear search is O(n) because it may check every value in the list
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Set the starting and ending indexes
    low = 0
    high = len(lst) - 1

    # Continue searching while there are values left to check
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Return the index if the target is found
        if lst[mid] == target:
            return mid

        # Search the right half if the target is larger
        if lst[mid] < target:
            low = mid + 1
        else:
            # Search the left half if the target is smaller
            high = mid -1

    # Return -1 if the target is not found
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # Create a small sorted dataset
    small_data = [10, 20, 30, 40, 50]

    # Search for a value that exists
    print("Linear search for 30:", linear_search(small_data, 30))
    print("Binary search for 30:", binary_search(small_data, 30))

    # Search for a value that does not exist
    print("Linear search for 35:", linear_search(small_data, 35))
    print("Binary search for 35:", binary_search(small_data, 35))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Create a much larger sorted dataset
    large_data = list(range(1, 1001))

    # Search for a value near the end of the dataset
    print("Linear search for 999:", linear_search(large_data, 999))
    print("Binary search for 999:", binary_search(large_data, 999))

    # Binary search is more efficient for large sorted datasets
    # because it cuts the remaining search area in half each time.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Create an empty list to test how the searches handle no data
    empty_data = []

    # Test an empty list
    print("Linear search empty list:", linear_search(empty_data, 10))
    print("Binary search empty list:", binary_search(empty_data, 10))

    # Test a single-element list
    single_data = [50]
    print("Linear search single-element list:", linear_search(single_data, 50))
    print("Binary search single-element list:", binary_search(single_data, 50))

    # EDGE CASE code is up here

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")

    # A teacher searches a sorted list of student scores
    student_scores = [65, 72, 78, 81, 85, 90, 95]

    # Use binary search to find the score 85
    result = binary_search(student_scores, 85)

    print("Student scores:", student_scores)
    print("Search for score 85:", result)


if __name__ == "__main__":
    main()
