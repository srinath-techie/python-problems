print("Welcomes You")
print("pls enter the bill amount")
amount =int(input())
print("your bill amount is :", amount)
if amount > 10000:
    discount = amount * 20/100
elif amount > 5000:
    discount = amount * 10/100
elif amount >= 1000:
    discount = amount * 5/100
else:
    discount = 0
print("You can only pay rs.",amount-discount)