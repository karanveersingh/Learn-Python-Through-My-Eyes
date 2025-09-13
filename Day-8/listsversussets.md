# Lists vs Sets in Python

## Lists

- **Ordered** collection of items
- **Allow duplicates**
- Elements can be accessed by index
- Mutable (can be changed)

```python
my_list = [1, 2, 2, 3]
print(my_list[1])  # Output: 2
```

## Sets

- **Unordered** collection of unique items
- **No duplicates allowed**
- No indexing or slicing
- Mutable (can add/remove items)

```python
my_set = {1, 2, 2, 3}
print(my_set)  # Output: {1, 2, 3}
```

## When to Use

- Use **lists** when order matters or duplicates are needed.
- Use **sets** for fast membership tests and unique elements.
