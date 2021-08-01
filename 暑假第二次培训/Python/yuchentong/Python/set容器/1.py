names=set(['Alice', 'Bob', 'Candy', 'David', 'Ellena'])
print(names)
name_set = set(names)
s=input('Input name')
s=s.capitalize()
if s in  name_set:
    print(True)
else:
    print(False)