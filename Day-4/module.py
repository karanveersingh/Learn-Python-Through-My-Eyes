# my_module.py
def add(a, b):
    return a + b

class MyClass:
    def __init__(self, value):
        self.value = value

# main_script.py
import my_module

result = my_module.add(5, 3)
print(result)

obj = my_module.MyClass(10)
print(obj.value)