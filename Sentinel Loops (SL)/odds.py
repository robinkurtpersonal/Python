print("odds")
user_times = int(input("How many odds do you want to list"))

selection = input("positive way or negative way")
while selection != "+" and selection != "-":
    print("invalid")
    selection = (input("positive way or negative way"))

# AND means that if I enter either +/-, it will fail

#positive way (1, 3 | starts (0-3) exits as 4)
if selection == "+":
    odd = 1
    counter = 0
    while counter < user_times: 
        print(odd) 
        odd += 2 
        counter += 1 

    

#negative way (-1,-3 | starts (0-3) exits as 4) 
elif selection == "-":
    odd = -1
    counter = 0
    while counter < user_times:
        print(odd)
        odd -= 2
        counter += 1
