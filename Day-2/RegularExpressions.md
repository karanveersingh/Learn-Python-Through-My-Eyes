# Regular Expressions  
To work with regular expressions in Python, you use the re module.
Regular expressions (regex) in Python are a powerful tool for pattern matching and manipulation of strings. Python's built-in re module provides support for regular expressions. Here's a quick overview:  

**Plan:**  
- Import the re module.  
- Use functions like re.match(), re.search(), re.findall(), or re.sub() to work with patterns.  
- Define patterns using raw strings (r"pattern") to avoid escaping backslashes.  

**Common re Module Functions:**
- re.search(pattern, string):
Scans through a string, looking for the first location where the pattern matches. Returns a match object if successful, None otherwise.  

- re.match(pattern, string):  
Determines if the pattern matches at the beginning of the string. Returns a match object if successful, None otherwise.  

- re.findall(pattern, string):  
Finds all non-overlapping matches of the pattern in the string and returns them as a list of strings.  

- re.sub(pattern, repl, string):  
Replaces all occurrences of the pattern in the string with repl.  

- re.split(pattern, string):  
Splits the string by occurrences of the pattern and returns a list of substrings.  

**Practical** 
import re

- Example 1: Match a pattern at the start of a string  
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
if match:
    print("Matched:", match.group())

- Example 2: Search for a pattern anywhere in the string  
search = re.search(r"world", text)
if search:
    print("Found:", search.group())

- Example 3: Find all occurrences of a pattern
text = "cat, bat, rat"
matches = re.findall(r"[cbr]at", text)
print("All matches:", matches)

- Example 4: Replace patterns in a string
text = "The rain in Spain"  
new_text = re.sub(r"ain", "123", text)  
print("Replaced text:", new_text)  

**Output**   
Matched: hello  
Found: world  
All matches: ['cat', 'bat', 'rat']  
Replaced text: The r123 in Sp123  