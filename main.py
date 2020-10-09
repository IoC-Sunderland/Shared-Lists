a = [1,2,3]
b = a
print(a == b) # True
print(a is b) # True

a.append(5)
print(a) # [1, 2, 3, 5]
print(b) # [1, 2, 3, 5] Hang on a minute!

b = a[:] # Intialise b with slice of a

print(a == b) # True
print(a is b) # False

b.append(6)
print(a) # [1, 2, 3, 5]
print(b) # [1, 2, 3, 5, 6] 

print(a == b) # True
print(a is b) # False