# While Loop Practical Examples

## 1. Counting Numbers

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

## 2. User Input Until Condition Met

```python
password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access granted!")
```

## 3. Summing Numbers

```python
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print("Sum:", total)
```

## 4. Infinite Loop with Break

```python
while True:
    response = input("Type 'exit' to quit: ")
    if response == "exit":
        break
```

## 5. Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```