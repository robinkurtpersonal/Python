#name and description
print("BSP_TaxationwithSetter")
print("Description: Allows you to set a Tax (enter in percentage)")

#amount (in float to count dirhams)
amount = float(input("Enter the amount (in QAR): "))

#tax_percentage = tax rate in % 
tax_percentage = int(input("Enter the tax amount (in percent): "))


#involves getting the amount and multiplying it to % to the same kind
tax_compute = amount * (tax_percentage/100)

#total finalized to pay
total_finalized_amount = amount + tax_compute

#outputs
print(f"Total Taxed Amount: {tax_compute:.2f} QAR")
print(f"Total Amount to pay {total_finalized_amount:.2f} QAR.")
