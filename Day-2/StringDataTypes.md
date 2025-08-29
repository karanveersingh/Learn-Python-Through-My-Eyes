## In Python, the string data type, represented as str, is used to handle textual data. Strings are sequences of Unicode characters and are fundamental for storing and manipulating text.

**Key Characteristics of Python Strings:**
**Definition:** Strings are created by enclosing a sequence of characters within single quotes ('...'), double quotes ("..."), or triple quotes ('''...''' or """...""") for multi-line strings.
**Example:**

    single_quote_string = 'Hello'
    double_quote_string = "World"
    multi_line_string = """This is a
    multi-line string."""

**Immutability:** Python strings are immutable, meaning that once a string is created, its content cannot be changed. Any operation that appears to modify a string actually creates a new string object.
**Example:**

    my_string = "Python"
    # my_string[0] = 'J' # This would raise a TypeError
    new_string = my_string.replace('P', 'J') # Creates a new string "Jython"

**Sequences:** Strings are sequences, allowing access to individual characters using indexing (starting from 0) and extracting substrings using slicing.
**Example:**

    text = "Example"
    print(text[0])   # Output: 'E'
    print(text[1:4]) # Output: 'xam'

**Methods:**
The str class provides numerous built-in methods for common string operations, such as:
    **len():** Returns the length of the string.
    **upper(), lower():** Convert to uppercase or lowercase.
    **find(), replace():** Search for substrings and replace them.
    **split(), strip():** Split strings into lists or remove leading/trailing whitespace.
    **startswith(), endswith():** Check if a string begins or ends with a specific substring.

**Concatenation and Repetition:**
Strings can be concatenated using the + operator and repeated using the * operator.
Python

    greeting = "Hello"
    name = "Alice"
    full_message = greeting + " " + name # "Hello Alice"
    repeated_char = "a" * 3 # "aaa"