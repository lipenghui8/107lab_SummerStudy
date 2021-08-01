names=['bob', 'about', 'Zoo', 'Credit']
i=0
for s in names:
    names[i]=s.lower()
    i+=1
print(sorted(names))