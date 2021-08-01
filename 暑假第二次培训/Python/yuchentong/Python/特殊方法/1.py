class Student():
    def __init__(self,name,gender,score):
        self.name=name
        self.gender=gender
        self.score=score
    def __str__(self):
        return 'Student:{},{},{}'.format(self.name,self.gender,self.score)
    def __repr__(self):
        return 'Student:{},{},{}'.format(self.name, self.gender, self.score)
bob=Student('bob','male','100')
print(str(bob))
print(repr(bob))