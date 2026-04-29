
# Write a program to fill in aletter template given below with name and date 

letter ='''Dear <|Name|>,
you are selected!
<|Date|>'''
           
           
print(letter.replace("<|Name|>", "Raj").replace("<|Date|>","05 March 2030"))  

     
print(letter.replace("<|Name|>", "Raj")) # it print only name and Strings not date