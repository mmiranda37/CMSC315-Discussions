"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Create an empty dictionary to store inventory items
    inventory = {}

    # A python dictionary behaves like a hash table by storing
    # information as key-value pairs
    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"]= 20
    inventory["P400"] = 12
    inventory["P500"] = 7

    # Display the inventory after inserting the items
    print("\nInventory:", inventory)

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Look up two existing SKUs using their keys
    # The dictionary uses each SKU key to retrieve its stored quantity
    print("P100 quantity:", inventory["P100"])
    print("P300 quantity:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Display the inventory before updating an item
    print("Before update:", inventory)

    # Assigning a new value to an existing key updates its value
    # instead of creating a duplicate key
    inventory["P100"] = 25

    # Display the inventory after the udpate
    print("After update:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Display the inventory before deleting an item
    print("Before deletion:", inventory)

    # Remove an existing SKU and its quantity from the inventory
    del inventory["P500"]

    # Display the inventory after the deletion
    print("After deletion:", inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Look up an SKU that does not exist
    # Using get() safely returns None instead of causing error
    missing_quantity = inventory.get("P999")
    print("Lookup missing P999:", missing_quantity)

    # Edge case 2: Try to delete an SKU that does not exist
    # Check for the key first so the program does not cause an error
    if "P999" in inventory:
        del inventory["P999"]
    else:
        print("P999 was not found so no item was deleted.")



if __name__ == "__main__":
    main()