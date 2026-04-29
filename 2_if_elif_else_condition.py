
score = int(input("Enter your Score: "))

if score >= 80:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")


if score %2==0:
    print("score is even!")
else:
    print("score is odd!")    


              #  With Extra elif Conditions
'''
score = int(input("Enter your Score: "))

if score >= 80:
    print("Grade A")
elif score >= 60 and score < 80:
    print("Grade B")
elif score >= 50 and score < 60:
    print("Grade C")
else:
    print("Fail")
    
    '''

              # In Sort using more elif conditions
'''               
score = int(input("Enter your Score: "))

if score >= 80:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")
'''


                        #  Using Except ValueError
                        
'''                        
try:
    score = int(input("Enter your Score: "))
    
    if score >= 80:
        print("Grade A")
    elif score >= 60:
        print("Grade B")
    elif score >= 50:
        print("Grade C")
    else:
        print("Fail")

except ValueError:
    print("Please enter only numbers!")

'''