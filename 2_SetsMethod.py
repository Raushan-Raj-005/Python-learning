items = {'apple','banana','papaya'}
print(items)

items.add('orange')
print(items)

items.update(['mango','grapes'])
print(items)

# items.remove('banana')   # No Error
# items.remove('bananae')   # Error because of Spelling mistackes
items.discard('bananae')   #  No Error

items.pop()      #remove random element from sets
print(items)
a=items.pop()
print(a)

print(len(items))


items.clear()
print(items)