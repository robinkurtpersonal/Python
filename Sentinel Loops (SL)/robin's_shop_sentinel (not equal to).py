#robin's_shop_sentinel (not equal to)

#initialization
total = 0

#validation
sale = int(input("Enter sale: "))

#condition
while sale != 0:
    #process
    total+=sale
    sale = int(input("Enter sale: "))




#output
print(f"The total sales is {total}")
