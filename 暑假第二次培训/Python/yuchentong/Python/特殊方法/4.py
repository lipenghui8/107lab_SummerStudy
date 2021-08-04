class Person():
    __slots__=('name','gender')
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Student(Person):
     __slots__=('name','gender','score')
     def __init__(self,name,gender,score):
          super(Student, self).__init__(name,gender)
          self.score=score
Bob=Student('Bob','man','100')
print(Bob.name,Bob.gender,Bob.score)
