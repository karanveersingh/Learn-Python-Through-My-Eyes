## Functions and modules are both fundamental concepts for organizing and reusing code, but they serve different purposes and operate at different levels of granularity.  

**Function:**  
A function is a self-contained block of reusable code designed to perform a specific task. It encapsulates a sequence of instructions, potentially taking input parameters and returning an output value. 
Functions are defined using the def keyword and are called by their name, often with arguments passed within parentheses

**Practical:**  
def greet(name):  
    """This function greets the given name."""  
    return f"Hello, {name}!"  

message = greet("Karan")  
print(message)  

NOTE: In this example, greet is a function that takes a name argument and returns a greeting message.

**Module:**
A module is a file containing Python code, which can include definitions of functions, classes, variables, and runnable statements.  
Modules serve as a way to logically organize related code and promote reusability across different programs or parts of a larger project.   
Modules are imported using the import statement, allowing access to their contents.  

Practical - 
- my_module.py
    def add(a, b):
    return a + b

class MyClass:
    def __init__(self, value):
    self.value = value

- main_script.py  
import my_module  

result = my_module.add(5, 3)
print(result)  

obj = my_module.MyClass(10)
print(obj.value)  

**Scope and Granularity:**  
A function is a smaller, more specific unit of code that performs a single task, while a module is a larger container that can hold multiple functions, classes, and variables, organizing them into a logical unit.  

**Purpose:**  
- Functions are used to encapsulate specific operations for reusability within a program.   
- Modules are used to organize and share collections of related code across different programs or larger projects.  

**Usage:**  
Functions are called by their name, while modules are imported to make their contents accessible.  

**File Structure:**  
Functions are defined within Python files (which can be modules), while modules are the Python files themselves.  

**Packages:**  
A package is a way of organizing related modules into a directory hierarchy. Essentially, a package is a directory that contains multiple Python modules and a special file named __init__.py. This __init__.py file signals to Python that the directory should be treated as a package.   

Packages allow for a hierarchical structuring of the module namespace using dot notation, similar to how files are organized in folders and subfolders on a computer.   

**Example:** A my_project package might contain subdirectories like database, views, and utilities, each containing relevant modules.  

**Practical**  
    my_project/  
    ├── __init__.py  
    ├── database/  
    │   ├── __init__.py  
    │   └── models.py  
    ├── views/  
    │   ├── __init__.py  
    │   └── web_views.py  
    └── utilities/  
        ├── __init__.py  
        └── helpers.py  

 **Import Python Module**
- This imports the entire module, and you access its contents using dot notation.
- Example

    - import module_name
    import math
    print(math.pi)

**Importing Specific Items from a Module.**
This imports only the specified functions, classes, or variables from a module, allowing direct access without the module prefix.
- Example

    - from module_name import item1, item2
    from math import pi, sqrt
    print(pi)
    print(sqrt(16))

**Importing an Entire Module with an Alias:**
This imports the entire module but assigns it a shorter, more convenient alias for use in your code.

    - import module_name as alias
    
    import pandas as pd
    df = pd.DataFrame()

**Importing Specific Items with Aliases.**
This imports specific items from a module and assigns them aliases.

    - from module_name import item as alias
   
    from cmath import sqrt as complex_sqrt
    print(complex_sqrt(-4))        