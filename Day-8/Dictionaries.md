# Dictionaries in Python

A **dictionary** is a built-in data type in Python that stores data as key-value pairs.

## Creating a Dictionary

```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

## Accessing Values

```python
print(my_dict["name"])  # Output: Alice
```

## Adding or Updating Items

```python
my_dict["email"] = "alice@example.com"  # Add new key-value pair
my_dict["age"] = 26  # Update existing value
```

## Removing Items

```python
del my_dict["city"]
```

## Looping Through a Dictionary

```python
for key, value in my_dict.items():
    print(key, value)
```

## Useful Dictionary Methods

- `keys()`: Returns all keys
- `values()`: Returns all values
- `items()`: Returns all key-value pairs

```python
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
```