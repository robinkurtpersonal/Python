print("Name: Convert a str to different cases: upper,lower,capitalize")
print("Description: utilizes .upper(), .lower(), and .capitalize() to convert it")


#input function | type: str | string to check
string = input("Enter your string: ")

#options board
print("1 - UPPERCASE")
print("2 - lowercase")
print("3 - capitalize")
#input function | type: str | select from options or not, print
option = input("Selection an option: ")

#conditions / instructions (only one is executed)

#condition 1 if   | UPPER
if option == "1":
    print(string.upper())
    
#condition 2 elif | lower
elif option == "2":
    print(string.lower())
    
#condition 3 elif | Capitalize
elif option == "3":
    print(string.capitalize())
#condition 4 else | non (always executes if non of the 3 are True)
else:
    print("Not in choices, please rerun the program again.")
    
