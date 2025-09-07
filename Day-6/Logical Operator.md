# Logical Operators in Python

Logical operators are used to combine conditional statements. Python has three logical operators:

| Operator | Description                        | Example                |
|----------|------------------------------------|------------------------|
| `and`    | Returns `True` if both are true    | `x > 5 and x < 10`     |
| `or`     | Returns `True` if one is true      | `x < 5 or x > 10`      |
| `not`    | Reverses the result, `True` to `False` | `not(x > 5)`      |

## Examples

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

Use logical operators to build complex conditions in your programs.