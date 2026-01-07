print("Evens")

user_number = int(input("How many evens do you want"))
selection = input("Positive or negative")
while selection != "positive" and selection != "negative":
    print("invalid")
    selection = input("Positive or Negative")

if selection == "positive":
    even = 2 # 2
    counter = 0 # 0
    while counter < user_number: # 0 | 1 | 2 | exit as 3
        print(even) # 2 4 6
        even += 2 # 4 6 8
        counter +=1 # 1 2 3
    
