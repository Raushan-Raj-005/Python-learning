amount = float(input("Enter purchase amount: "))

if amount == 0:
    print("Not required Bill")
elif 0 < amount <= 100:
    discount = amount*0.05
elif 101 <= amount <= 1000:
    discount= amount*0.10
elif 1001 <= amount <= 10000:
    discount= amount*0.20
else:  
    discount= amount*0.30  


if amount >0:
    total_amount = amount-discount
    
    print("Total amount to pay: ",total_amount)               