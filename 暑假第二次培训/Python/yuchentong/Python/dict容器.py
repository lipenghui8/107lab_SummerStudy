# d = {
#     'Alice': 45,
#     'Bob': 60,
#     'Candy': 75,
#     'David': 86,
#     'Ellena': 49,
#     'Gaven':86
# }
#print(d)
#print(d.get('Alice'),d.get('Bob'),d.get('Candy'),d.get('Mimi'),d.get('David'))
#d['Alice']=[45,60]
#print(d)
# key=d.keys()
# s=input('input name')
# if s not in key:
#     pass
# else:
#     d.pop(s)
# print(d)
# d = {'Alice': [50, 61, 66], 'Bob': [80, 61, 66], 'Candy': [88, 75, 90]}
# for key in d:
#     for value in d[key]:
#         print(key,value)
num=0
for key in d.values():
   for val in key:
       num+=1
print(num)