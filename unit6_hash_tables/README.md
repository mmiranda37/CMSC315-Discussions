# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation
I created an inventory system using a Python dictionary to demonstrate how dictionaries behave like hash tables. The inventory stored SKU numbers as keys and item quantities as values. I added five inventory items and demonstrated lookup, update, and delete operations.

I also tested edge cases by looking up an SKU that did not exist and attempting to safely delete an SKU that was not in the inventory. The "get()" method returned "None" for the missing SKU, and I checked whether a key existed before attempting to delete it.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.