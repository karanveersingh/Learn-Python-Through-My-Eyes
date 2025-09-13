# Sets in Python

A **set** is an unordered collection of unique elements in Python.

## Creating a Set

```python
my_set = {1, 2, 3}
empty_set = set()
```

## Key Features

- **No duplicates:** Each element is unique.
- **Unordered:** No indexing or slicing.
- **Mutable:** You can add or remove elements.

## Common Operations

```python
# Add an element
my_set.add(4)

# Remove an element
my_set.remove(2)

# Check membership
print(3 in my_set)  # True

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
```

## When to Use Sets

- Removing duplicates from a list
- Fast membership testing
- Performing mathematical set operations
