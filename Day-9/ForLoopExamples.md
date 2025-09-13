# For Loop: Practical Approach

## Basic Syntax

```python
for item in iterable:
    # Code block to execute
```

## Examples

### 1. Looping Through a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2. Using `range()`

```python
for i in range(5):
    print(i)
```

### 3. Summing Numbers in a List

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Sum:", total)
```

### 4. Iterating Over a String

```python
for char in "Python":
    print(char)
```

### 5. Nested For Loops

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

## Practical Tips

- Use `break` to exit a loop early.
- Use `continue` to skip to the next iteration.
- Combine with `enumerate()` for index and value.

```python
for idx, val in enumerate(fruits):
    print(idx, val)
```