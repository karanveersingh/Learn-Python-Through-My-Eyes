# Type Conversions in Python

Type conversion refers to changing the data type of a value to another data type.

## Types of Type Conversion

### 1. Implicit Type Conversion
Python automatically converts one data type to another without user intervention.

```python
a = 5      # int
b = 2.0    # float
result = a + b  # result is float (7.0)
print(type(result))  # <class 'float'>
```

### 2. Explicit Type Conversion (Type Casting)
The user manually converts one data type to another using built-in functions.

#### Common Functions:
- `int()`
- `float()`
- `str()`
- `bool()`
- `list()`, `tuple()`, `set()`, etc.

#### Examples:

```python
x = "10"
y = int(x)      # Converts string to integer
z = float(x)    # Converts string to float
s = str(25)     # Converts integer to string
```

## Example Table

| Function   | Description                | Example         | Result      |
|------------|---------------------------|-----------------|-------------|
| `int()`    | Converts to integer       | `int("5")`      | `5`         |
| `float()`  | Converts to float         | `float("3.14")` | `3.14`      |
| `str()`    | Converts to string        | `str(100)`      | `"100"`     |
| `bool()`   | Converts to boolean       | `bool(0)`       | `False`     |

## Notes
- Not all conversions are possible (e.g., `int("abc")` raises an error).
- Use type conversion carefully to avoid unexpected results.
