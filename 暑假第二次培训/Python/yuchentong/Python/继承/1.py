class Person():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course=course
bob=Teacher('Bob','man','math')
print(bob.name,bob.gender,bob.course)