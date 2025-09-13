# String to List Conversion in Python

Converting a string to a list is a common operation in Python. Here are some typical methods:

## 1. Using `list()`

Converts a string into a list of its characters.

```python
s = "hello"
lst = list(s)
print(lst)  # Output: ['h', 'e', 'l', 'l', 'o']
```

## 2. Using `split()`

Splits a string into a list based on a delimiter (default is whitespace).

```python
s = "apple banana cherry"
lst = s.split()
print(lst)  # Output: ['apple', 'banana', 'cherry']
```

You can specify a custom delimiter:

```python
s = "apple,banana,cherry"
lst = s.split(',')
print(lst)  # Output: ['apple', 'banana', 'cherry']
```

## 3. List Comprehension

For custom conversions, such as splitting and processing:

```python
s = "1 2 3 4 5"
lst = [int(x) for x in s.split()]
print(lst)  # Output: [1, 2, 3, 4, 5]
```

---

**Summary:**  
- Use `list()` for characters.  
- Use `split()` for words or custom delimiters.  
- Use list comprehensions for advanced processing.