
                        # Create file and Write funcition

# a = "raushan is a good student"
# file = open("Raushan.txt", "w")
# file.write(a)
# file.close()

                       # Search file and Read funcition

file = open("Raj.txt", "r")
content = file.read()
print(content)
file.close()


file = open("Raj.txt", "r")
# content = file.read()
content = file.readlines()
# content = file.readline()
print(content)
file.close()
