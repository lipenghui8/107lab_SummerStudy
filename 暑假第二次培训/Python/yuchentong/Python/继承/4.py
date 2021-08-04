class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.items():
            setattr(self, k, v)

    def get_info(self):
        return 'name={}\ngender={}'.format(self.name, self.gender)


p = Person('Bob', 'male', age=18, course='python')
print(p.get_info())
print(p.age)
print(p.course)