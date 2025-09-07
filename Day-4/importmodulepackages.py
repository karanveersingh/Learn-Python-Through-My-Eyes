#This imports the entire module, and you access its contents using dot notation.


#import module_name
# Example:
import math
print(math.pi)

#Importing Specific Items from a Module.
#This imports only the specified functions, classes, or variables from a module, allowing direct access without the module prefix.


#from module_name import item1, item2
# Example:
from math import pi, sqrt
print(pi)
print(sqrt(16))

#Importing an Entire Module with an Alias:
#This imports the entire module but assigns it a shorter, more convenient alias for use in your code.
#import module_name as alias
# Example:
import pandas as pd
df = pd.DataFrame()
print(df)

#Importing Specific Items with Aliases.
#This imports specific items from a module and assigns them aliases.


#from module_name import item as alias
# Example:
from cmath import sqrt as complex_sqrt
print(complex_sqrt(-4))