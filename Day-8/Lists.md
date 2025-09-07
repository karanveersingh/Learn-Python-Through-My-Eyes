# Lists in Python

A **list** in Python is an ordered, mutable collection of items. Lists can store elements of different data types.

## Creating a List

```python
my_list = [1, 2, 3, 'apple', True]
```

## Accessing Elements

```python
print(my_list[0])  # Output: 1
print(my_list[-1]) # Output: True
```

## Modifying Lists

```python
my_list.append('new item')   # Add to end
my_list[1] = 'changed'       # Modify element
del my_list[2]               # Remove by index
```

## List Methods

- `append(item)` – Add item to end
- `insert(index, item)` – Insert at position
- `remove(item)` – Remove first occurrence
- `pop(index)` – Remove and return item
- `sort()` – Sort the list

## Example

```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
```