class Animal(object):
    def __init__(self, name, age, location):
        self.__name = name
        self.__age = age
        self.__location = location

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_location(self):
        return self.__location

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_location(self, location):
        self.__location = location
    def set_into(self):
        return 'name:{},age:{},location:{}'.format(self.__name,self.__age,self.__location)


dog = Animal('wang', '1', 'henan')
print(dog.get_name(), dog.get_age(), dog.get_location())
dog.set_name('miao')
print(dog.set_into())