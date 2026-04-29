# print("Intlizing.....")

# a = int(input("Enter a : \n"))
# b = int(input("Enter b : \n"))
# try:
#     print("The value of a/b is: ", a/b)
# except:
#     print("Some error occured!")    
# print("Thanks......")    
        
        
        
print("Intlizing.....")

a = int(input("Enter a : \n"))
b = int(input("Enter b : \n"))
try:
    print("The value of a/b is: ", a/b)
except Exception as e:
    print("Some error occured - ",e)    
print("Thanks......")    
                