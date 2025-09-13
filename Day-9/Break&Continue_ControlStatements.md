# Break and Continue Statements in Python

Control statements like `break` and `continue` are used to alter the flow of loops.

## `break` Statement

- **Purpose:** Exits the nearest enclosing loop immediately.
- **Usage Example:**
    ```python
    for i in range(5):
            if i == 3:
                    break
            print(i)
    # Output: 0 1 2
    ```

## `continue` Statement

- **Purpose:** Skips the rest of the current loop iteration and moves to the next iteration.
- **Usage Example:**
    ```python
    for i in range(5):
            if i == 3:
                    continue
            print(i)
    # Output: 0 1 2 4
    ```

## When to Use

- Use `break` to stop a loop when a condition is met.
- Use `continue` to skip certain iterations based on a condition.

## Practical Approach

Consider searching for a specific item in a list. You can use `break` to stop searching once the item is found, or `continue` to skip unwanted items.

```python
numbers = [1, 3, 5, 7, 9, 2, 4]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
```
*This loop stops at the first even number.*

```python
for num in numbers:
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")
```
*This loop prints only the odd numbers, skipping even ones.*