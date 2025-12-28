#name and description
print("BSP_DiscountwithSetter")
print("Description: Allows you to set a discount (enter in percentage)")

#amount (in float to count dirhams)
amount = float(input("Enter the amount (in QAR): "))

#discount_percentage = discount rate in % 
discount_percentage = int(input("Enter the discount amount (in percent): "))


#involves getting the amount and multiplying it to % to the same kind
discount = amount * (discount_percentage/100)

#total finalized to pay
total_finalized_amount = amount - discount

#outputs
print(f"Total Discounted Amount: {discount:.2f} QAR")
print(f"Total Amount to pay {total_finalized_amount:.2f} QAR.")
