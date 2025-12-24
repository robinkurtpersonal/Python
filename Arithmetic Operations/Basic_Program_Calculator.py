#name & description
print("Name: Basic_Program_Calculator ")
print("Description: Solve for Addition / Subtraction / Multiplication / Division ")
print("")

#basic_program 
integer_one = int(input("Enter the first integer: "))
integer_two = int(input("Enter the second integer: "))
choice = input("Enter Choice: add/subtract/multiply/divide: ")

if choice == "add":
    sumint = integer_one + integer_two
    print(f"The total sum is {sumint}.")
    
elif choice == "subtract":
    differenceint = integer_one - integer_two
    print(f"The total difference is {differenceint}.")
    
elif choice == "multiply":
    multiplyint = integer_one * integer_two
    print(f"The total product is {multiplyint}.")

elif choice == "divide":
    divideint = integer_one / integer_two
    print(f"The total quotient is {divideint}.")

else:
    print("Option not available.")
    print("Please rerun the program.")



#end of basic_program


#signature & trademark
print("")
print("Program Finished. Copyright RKCA 2025")
