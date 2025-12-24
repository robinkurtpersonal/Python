#name & description
print("Name: Simple_Decision ")
print("Description: Cashier - Customer Bill Relationship | Give 10% discount if purchase amount more than 1000 ")
print("")

#----------------------------basic_program-------------------------------- 
amount = int(input("What is your purchase amount? "))


if amount > 1000:
    amount = amount - (0.1 * amount)
    

print(f"You are required to pay {amount}")

#----------------------------end of basic_program-------------------------


#signature & trademark
print("")
print("Program Finished. Copyright RKCA 2025")

#NOTES
#if condition (executes only if am > 1000)
#amount is either the same or modified to be discounted
