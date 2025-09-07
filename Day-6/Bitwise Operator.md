# Bitwise Operators in Python

Bitwise operators are used to perform operations on individual bits of integer values.

| Operator | Name            | Description                          | Example (`a = 5`, `b = 3`) |
|----------|-----------------|--------------------------------------|----------------------------|
| `&`      | AND             | Sets each bit to 1 if both are 1     | `a & b` → `1`              |
| `|`      | OR              | Sets each bit to 1 if one is 1       | `a | b` → `7`              |
| `^`      | XOR             | Sets each bit to 1 if only one is 1  | `a ^ b` → `6`              |
| `~`      | NOT             | Inverts all the bits                 | `~a` → `-6`                |
| `<<`     | Left Shift      | Shifts bits left, adds 0s on right   | `a << 1` → `10`            |
| `>>`     | Right Shift     | Shifts bits right, discards rightmost| `a >> 1` → `2`             |

## Example

```python
a = 5      # 0b0101
b = 3      # 0b0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2
```