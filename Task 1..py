# Instant Discount System
print("Welcome to the Instant Discount System")
cost=float(input("Enter the total amount: "))
if cost < 100:
    discount=0
elif cost>=100 and cost < 500:
    discount=0.10
else:
    discount=0.20
discountValue=cost*discount
finalPrice=cost-discountValue
print(f"your discount is: {discountValue}")
print(f"final price after discount: {finalPrice}")
    


