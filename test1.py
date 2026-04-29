days = int(input("Enter days: "))
rent =0

if days<=4:
    rent= days*600
elif days<=8:
    rent= (4*600)+(days-4)*400 
elif days<=12:
    rent= (4*600)+(4*400)+(days-8)*200
else:
    rent=(4*600)+(4*400)+(4*200)+(days-12)*200
    
print("Total rent : ", rent)               