#Datatype conversions

variable = 5
print(int(variable))

print(float(variable))

print(str(variable))

#basically all of these is possible except turning
# str (sentence/text/symbols/etc) into int/float
# turning str float into an int

variable = "5.0"
# print(int(variable))
# ValueError: invalid literal for int() with base 10: '5.0'

#print(float("hi"))
# ValueError: could not convert string to float: 'hi'
