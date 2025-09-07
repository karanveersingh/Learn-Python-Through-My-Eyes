# Membership Operators in Python

Membership operators are used to test if a sequence (such as a string, list, tuple, or dictionary) contains a specified value.

## Operators

| Operator | Description                              | Example           |
|----------|------------------------------------------|-------------------|
| `in`     | Returns `True` if value is present       | `'a' in 'apple'`  |
| `not in` | Returns `True` if value is not present   | `3 not in [1,2,4]`|

## Examples

```python
# Using 'in'
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # Output: True

# Using 'not in'
numbers = [1, 2, 3, 4]
print(5 not in numbers)    # Output: True

# With strings
text = "hello world"
print('world' in text)     # Output: True
```

## Use Cases

- Checking if an item exists in a list
- Verifying if a substring exists in a string
- Validating dictionary keys
