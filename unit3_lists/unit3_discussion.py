"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the specified index.
    # Existing elements at and after the index are shifted one position to the right.
    # Inserting near the beginning may take longer because more elements must be shifted.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check that the index exists before attempting to remove an item.
    if 0 <= index < len(lst):
        # Remove and return the value at the specified index.
        removed_value = lst.pop(index)
        return removed_value

    # Return None when the index is outside the valid range.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Check each element in the list one at a time.
    # This is a linear search because the list is scanned sequentially until the value is found.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 if the value was not found in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create a list with several starting values.
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert a value at the beginning of the list.
    insert_at(numbers, 0, 5)
    print("After beginning insertion:", numbers)

    # Insert a value into the middle of the list.
    insert_at(numbers, 2, 15)
    print("After middle insertion:", numbers)

    # Insert a value at the end of the list.
    insert_at(numbers, len(numbers), 50)
    print("After end insertion:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Delete the first item and display the removed value and updated list.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Delete an item from the middle and display the results.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Delete the last item and display the results.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for a value that exists in the list.
    existing_value = 20
    result = search_value(numbers, existing_value)
    print(existing_value, "was found at index", result)

    # Search for a value that does not exist in the list.
    missing_value = 100
    result = search_value(numbers, missing_value)
    print(missing_value, "was not found. Search result:", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Try to delete an item using an invalid index.
    invalid_result = delete_at(numbers, 100)
    print("Delete with invalid index:", invalid_result)

    # Edge case 2: Insert a value into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 10)
    print("Insert into empty list:", empty_list)

print("\n=== REAL-WORLD SCENARIO: MUSIC PLAYLIST ===")

# A music playlist is a real-world example of a list.
playlist = ["Song A", "Song B", "Song C"]
print("Original playlist:", playlist)

# Add a new song to the end of the playlist.
insert_at(playlist, len(playlist), "Song D")
print("After adding a song:", playlist)

# Search for a song in the playlist.
song_index = search_value(playlist, "Song B")
print("Song B was found at index", song_index)

# Remove a song from the playlist.
removed_song = delete_at(playlist, 0)
print("Removed song:", removed_song)
print("Updated playlist:", playlist)

if __name__ == "__main__":
    main()