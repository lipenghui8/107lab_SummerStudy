# Enter a code
class Animal(object):
    count=0
    def __init__(self,name):
        self.name=name
        self.__count+=1
    @classmethod
    def get_count(cls):
        return cls.__count
dog=Animal('wang')
print(dog.get_count())