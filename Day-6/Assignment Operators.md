# Assignment Operator in Python

Assignment operators are used to assign values to variables. The most common assignment operator is `=`, but Python provides several compound assignment operators as well.

## Basic Assignment

```python
x = 5  # Assigns the value 5 to variable x
```

## Compound Assignment Operators  

| Operator | Example   | Equivalent To |
|----------|-----------|--------------|
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 2`  | `x = x - 2`  |
| `*=`     | `x *= 4`  | `x = x * 4`  |
| `/=`     | `x /= 2`  | `x = x / 2`  |
| `%=`     | `x %= 3`  | `x = x % 3`  |
| `//=`    | `x //= 2` | `x = x // 2` |
| `**=`    | `x **= 3` | `x = x ** 3` |
| `&=`     | `x &= 2`  | `x = x & 2`  |
| `|=`     | `x |= 2`  | `x = x \| 2` |
| `^=`     | `x ^= 2`  | `x = x ^ 2`  |
| `>>=`    | `x >>= 1` | `x = x >> 1` |
| `<<=`    | `x <<= 1` | `x = x << 1` |

## Example

```python
x = 10
x += 5  # x is now 15
x *= 2  # x is now 30
```