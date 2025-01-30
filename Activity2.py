buyingprice = float(input("Enter the buying price: "))
sellingprice = float(input("Enter the selling price: "))

if sellingprice > buyingprice:
    amount = sellingprice - buyingprice
    print("Total profit: ",amount)

else:
    print("No profit")
