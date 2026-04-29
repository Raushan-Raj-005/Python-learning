try:
    x=int(input("Enter a number: "))
    y=10/x
except ValueError:
    print("Please enter a vlid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("I will always run & i am using when i am written inside the function ")            