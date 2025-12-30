print("Average_Solver_V1.0.0")
print("Description: Solves the average of a number input by user")


#initialization
counter = 0
total_sum = 0

#inputs
no_of_numbers = int(input("How many numbers will you want to compute: "))

#while (user-defined counted loop)
while counter < no_of_numbers:
    each_number = float(input("Enter number: "))
    total_sum += each_number
    counter += 1
    
#average formula
average = total_sum / counter

#output
print(f"The average of your inputs is {average}")
