#variable -> u cannot start with number / symbol

# 2variable 
# %variable

#both result in the following: SyntaxError: Invalid Syntax

#python is case sensitive
variable = 1
Variable = 2
print(variable)
print(Variable)
# print(VARIABLE) - NameError: name 'VARIABLE' is not defined
