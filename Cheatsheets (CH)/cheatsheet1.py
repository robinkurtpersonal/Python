#this is a comment

#Several ways to print

#comma method (seperate arguments)
print("Hello!","World!")

#concatenation for strings
print("Hello"+" "+"World")

#variables
num = 2 # int == integer
dec = 2.0 # float == decimal (floating point number)
sentence = "Robin" # str == string
b = True # bool == boolean (True/False)

#variable naming conventions
vartextonly = "check"
_varundstart = "check"
varundend_ = "check"
number2 = "check"
all_in_3 = "check"

# 2var = "no" WILL NOT WORK (number)
# $var = "no" WILL NOT WORK (symbol)
#if = "no" WILL NOT WORK (reserved word)

#Variables Case Sensitivity
Variable = "a"
variable = "b"
# These are different

#Numeric Expressions
#Classic Arithmetic Operations

#addition +
print(1+1)
#subtraction -
print(1-1)
#multiplication *
print(1*5)
#division (decimal/float) /
print(10/5)
#division (integer) //
print(10//5)

#other arithmetic operations

#power ** (base - exponent)
print(3**2)
#remainder %
print(10%3)

#operations between a float and a integer == always returns a float
print(1*1.0)

variable_test = "1"
print(float(variable_test))
print(int(variable_test))


print(1+6/2*2**3)
#for this one
#power -> division -> multiplication -> addition

#converting datatypes

#string int convert
print(int("10"))
print(float("10"))

#string float convert
print(int("10.0")) #error
print(float("10.0")) 

#int convert
print(str(10))
print(float(10))

#float convert
print(str(10.0))
print(int(10.0))

#input function
#default: str
variable = input("Enter: ")

#int input function
variable = int(input("Enter integer: "))

