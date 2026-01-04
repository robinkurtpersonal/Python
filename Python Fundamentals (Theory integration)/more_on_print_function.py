#more on print function
date = 16


# + concatenation (always requires non-str variables on conversion
print("My Birthday is on the " + str(date)+"th")

# , seperate arguments = acts as single space (no conversion) 
# limitation: hard to get things to stick
print("My Birthday is on the",date,"th")

# f - string = simplify printing values and variables
#format print(f"text {variable}")
#easiest to understand if you do it properly
print(f"My birthday is on the {date}th")
