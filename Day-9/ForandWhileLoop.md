# For Loop in Python

**for loop** in Python is used to iterate over a sequence (like a list, tuple, string, or range).

## Basic Syntax

```python
for variable in sequence:
    # code block to execute
```

## Example: Looping through a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## Example: Using `range()`

```python
for i in range(5):
    print(i)
```
_Output:_
```
0
1
2
3
4
```

## Notes

- The loop variable takes the value of each item in the sequence, one by one.
- Indentation is important in Python to define the code block inside the loop.

# While Loop in Python

The **while loop** in Python repeatedly executes a block of code as long as a given condition is `True`.

## Basic Syntax

```python
while condition:
    # code block to execute
```

## Example: Counting with a while loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```
_Output:_
```
0
1
2
3
4
```

## Notes

- The loop continues until the condition becomes `False`.
- Be careful to update variables inside the loop to avoid infinite loops.
- Indentation is required to define the loop body.
