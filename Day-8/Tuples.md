# Tuples in Python

A **tuple** is an immutable sequence type in Python. Tuples are similar to lists, but unlike lists, their elements cannot be changed after creation.

## Creating a Tuple

```python
my_tuple = (1, 2, 3)
empty_tuple = ()
single_element_tuple = (5,)  # Note the comma
```

## Accessing Tuple Elements

You can access elements by index:

```python
print(my_tuple[0])  # Output: 1
```

## Tuple Operations

- **Concatenation:** `a + b`
- **Repetition:** `a * 3`
- **Slicing:** `a[1:3]`

## Tuple Methods

Tuples support only two methods:

- `count(x)`: Returns the number of times `x` appears.
- `index(x)`: Returns the index of the first occurrence of `x`.

## Immutability

Tuples cannot be changed after creation:

```python
my_tuple[0] = 10  # Raises TypeError
```

## When to Use Tuples

- When you need an immutable sequence.
- As keys in dictionaries (if all elements are hashable).
- To return multiple values from a function.
