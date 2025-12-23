#name & description
print("Name: Basic_Program_Calculator ")
print("Description: Solve for Addition / Subtraction / Multiplication / Division ")
print("")

#basic_program 

#enter 2 integers
integer_one = int(input("Enter the first integer: "))
integer_two = int(input("Enter the second integer: "))

#enter a choice (add/subtract/multiply/divide)
choice = input("Enter Choice: add/subtract/multiply/divide: ")

#addition
if choice == "add":
    sumint = integer_one + integer_two
    print(f"The total sum is {sumint}.")

#subtraction
elif choice == "subtract":
    differenceint = integer_one - integer_two
    print(f"The total difference is {differenceint}.")

#multiplication
elif choice == "multiply":
    multiplyint = integer_one * integer_two
    print(f"The total product is {multiplyint}.")

#division
elif choice == "divide":
    divideint = integer_one / integer_two
    print(f"The total quotient is {divideint}.")

#---executes if you type something not on the list---
else:
    print("Option not available.")
    print("Please rerun the program.")



#end of basic_program


#signature & trademark
print("")
print("Program Finished. Copyright RKCA 2025")
