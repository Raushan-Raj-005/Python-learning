x=95               # Global Variable
def show_value():
    global x          # Global Keywords :- Use to modify the value of global variable
    x=950            
    print(x)
    
show_value()
show_value() 
print(x) 