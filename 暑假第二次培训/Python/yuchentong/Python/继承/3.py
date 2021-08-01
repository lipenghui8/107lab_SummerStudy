class Person():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student, self).__init__(name,gender)
        self.score=score
class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher, self).__init__(name,gender)
        self.course=course
class SkillMixin():
    def __init__(self):
        pass
class BasketballMixin(SkillMixin):
    def __init__(self):
        super(BasketballMixin, self).__init__()
class FootballMixin(SkillMixin):
    def __init__(self):
        super(FootballMixin, self).__init__()

class bassketball_student(BasketballMixin,Student):
    pass
class football_teacher(FootballMixin,Teacher):
    pass


