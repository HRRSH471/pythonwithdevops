
# Taking Cost and selling price from user

cost_price=int(input("Enter the cost price of the product "))
selling_price=int(input("Enter the selling price of the "))

if cost_price < selling_price:
    profit=selling_price-cost_price
    print("Profit=",profit)
elif cost_price>selling_price:
    loss=cost_price-selling_price
    print("Loss=",loss)
else:

 print("No Profit No loss")
