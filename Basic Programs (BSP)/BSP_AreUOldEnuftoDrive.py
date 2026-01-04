print("Are you old enough to drive?")

age = int(input("How old are you? "))

if age >= 18:
    print("Yes you can drive.")
elif age >= 16:
    print("Consider getting a student license.")
else:
    print("No, you are not allowed to drive.")
