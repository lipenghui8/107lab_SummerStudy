def info(**l):
    names=l['names']
    genders=l['gender']
    ages=l['age']
    i=0
    for name in names:
        gender=genders[i]
        age=ages[i]
        print('name: {},gender: {},age: {}'.format(name, gender, age))
        i+= 1

info(names = ['Alice', 'Bob', 'Candy'], gender = ['girl', 'boy', 'girl'], age = [16, 17, 15])