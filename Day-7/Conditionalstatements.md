Conditional statements allow you to execute certain blocks of code based on specific conditions.

## `if` Statement

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `if-else` Statement

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## `elif` Statement

```python
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Nested Conditionals

```python
x = 8
if x > 0:
    if x < 10:
        print("x is a positive single-digit number")
```

## Summary

- Use `if` to check a condition.
- Use `elif` for additional conditions.
- Use `else` for all other cases.
