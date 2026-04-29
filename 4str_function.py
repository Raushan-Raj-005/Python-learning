name = "Raushan"

print(len(name))    # find length of string


# string endwith
print(name.endswith("han"))
print(name.endswith("ha"))

# string startwith
print(name.startswith("Ra"))
print(name.startswith("ra"))   # false due to regions of small character
print(name.startswith("ha"))


# capitalize first letter only
word = "raj"
print(word.capitalize())


print("Most string function in python is:")

s = "  Hello World!  "

print(s.strip())    # Removes whitespace from both ends
print(s.lstrip())    # Removes whitespace from the left side
print(s.rstrip())   # Removes whitespace from the right side

print(s.lower())   # Converts string to lowercase
print(s.upper())   # Converts string to uppercase


print(s.title() )         # Makes Every Word Start With Capital Letter
print(s.capitalize())     # Capitalizes only the first character


print(s.replace("World", "Python"))  # Replace substring with another



print(s.split() )             # Splits string into list on spaces
",".join(["a","b"])          # Joins list into string with commas



print(s.find("World"))    # Returns starting index (or -1 if not found)
print(s.index("World"))   # Same but throws error if not found


print(s.count("l") )   # Counts occurrences of substring


print("---hello---".strip("-"))   # Removes specific characters




print("123".isdigit() )    # True if all characters are digits
print("abc".isalpha() )    # True if only letters
print("abc123".isalnum())  # True if letters + numbers
"   ".isspace()   # True if only whitespace


name="Ram"

print(name)
print(len(name))
print(name.isalpha())
print(name.isnumeric())