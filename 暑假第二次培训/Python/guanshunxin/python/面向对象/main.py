# class Person:
#     def __init__(self1,name,age,height,weight):#self1是命名的结构体名
#         self1.name=name
#         self1.age=age
#         self1.height=height
#         self1.weight=weight
#     def print_person(self1):
#         print("姓名",self1.name)
#         print("年龄",self1.age)
#         print("身高",self1.height)
#         print("体重",self1.weight)
# person=Person('管大爷',18,180,60)
# person.print_person()
# class Dog:
#     def __init__(self):
#         print("汪汪汪！")
# dog=Dog()
#初始化一些属性
# class Dog:
#     def __init__(self,name):
#         self.name=name
#         self.age=12
# dog=Dog("旺财")
# print(dog.age)
# print(dog.name)
#在类中定义的函数为方法
# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def play(self):
#             print("汪汪汪!我是:",self.name)
# dog=Dog("李耀华")
# dog.play()
#__name两条下划线不能直接访问为私有属性
# class Dog:
#     def __init__(self,name):
#         self.__name=name
#     def play(self):
#         print("汪汪汪！",self.__name)
# dog=Dog("金子淳")
# dog.play()
# print(dog.__name)#报错了
# class Dog:
#     def __init__(self,name):
#         self.__name=name
#         self.__age=None
#         print(self.__name,"出生了")
#     def set_age(self,age):
#         if not isinstance(age,int):
#             print("s输入年龄必须是数字")
#             return False
#         if age<0:
#             print("年龄大于0!")
#             return False
#         self.__age=age
#     def play(self):
#         print("汪汪汪！我今年",self.__age,"了！")
# dog=Dog("金子淳")
# dog.set_age("hello")
# dog.set_age(-10)
# dog.set_age(3)
# dog.play()
#私有方法
# class Dog:
#     def __say(self,name):
#         print(name)
#     def play(self):
#         self.__say("汪汪汪")
# dog=Dog()
# dog.play()#可以运行所以只能在类内修改
# dog.__say()#报错
#继承和多态
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def play(self):
#         print("我是：",self.name)
# class Dog(Animal):
#    def __init__(self):
#        super(Dog, self).__init__("旺财")
# dog=Dog()
# dog.play()
#子类不能继承父类的私有方法也不能调用
#多态
# class Animal:
#     def __init__(self):
#         def say(self):
#             print("animal")
# class Dog(Animal):
#     def say(self):
#         print("dog")
# class Cat(Animal):
#     def say(self):
#         print("cat")
# def animal_say(animal):
#     animal.say()
# dog=Dog()
# dog.say()
# cat=Cat()
# cat.say()#他们都调用了自己的say，子类方法会覆盖父类
# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))
# print(isinstance(cat,Animal))
# print(isinstance(cat,Cat))#他们都是继承下的
# animal_say(dog)
# animal_say(cat)
#类变量
# class Animal:
#     name="giao华"
# print(Animal.name)
# dog=Animal()
# cat=Animal()
# print(dog.name)
# print(cat.name)
# Animal.name="giao金"#可对类变量调用
# print(dog.name)
# print(dog.name)
#静态方法
# class Animal:
#     name="giao金"
#     @staticmethod
#     def play():
#         print("playing")
# Animal.play()
# class Animal:
#     name="giao华"
#     @classmethod
#     def play(cls):
#         print(cls.name,"playing")
# Animal.play()

