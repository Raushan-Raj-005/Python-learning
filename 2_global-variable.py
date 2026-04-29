x=75               # Global Variable
def show_value():
    print(x)
    
show_value()
show_value()    





x=25               # Global Variable
def show_value():
    x=30            # Local Variable
    print(x)
    
show_value()
show_value() 
print(x) 