#函数
# def introduce(name):
#   print("hello",name)
# introduce("管大爷")
# introduce("world")
# def add(a,b):
#     print("a+b=",a+b)
# add(2,3)
#关键字参数,使用关键字可以无视顺序
# def hello(name,age):
#     print("姓名",name)
#     print("年龄",age)
# hello("李耀华",99)
# hello(age=12,name="管大爷")
#默认参数(必须定义在最后)，可以在参数没传够情况下
# def dd(name,age=18):
#     print("我的名字是：",name)
#     print("年龄",age)
# dd("净资产")
#可变参数
# def foo(*args):#*args传的是元组
#     print(args)
# foo()
# foo(1,2)
# foo("管大爷","shanghai",22)
# def foo(**args):#**args传的是字典
#     print(args)
# foo()
# foo(name="管大爷")
# def cal(*args,**kwargs):
#     s=0
#     for i in args:
#         s+=i
#     print("输出的数字和是",s)
#     for k,v in kwargs.items():
#         print(k,v)
# cal(1,2,3,4,5,姓名="管大爷")
# def exp(*args,**kwargs):
#     print(args)
#     print(kwargs)
# l=(1,2,3,4)#l=[1,2,3,4]
# m={"管大爷":"爸爸","刘星宇":"儿子"}
# exp(*l,**m)
#局部变量
# def foo():
#     x="hello"#在函数内定义的和参数都是局部变量
#     print(x)
# foo()
# x="函数体外"
# def foo():
#     x="函数体内"
#     print(x)
# foo()
# print(x)
#要想修改外面的变量用global
# x="函数体外"
# def foo():
#     global x
#     x="函数体内"
#     print(x)
# foo()
# print(x)
#返回值
# def foo():
#     x="局部变"
#     return x
# result=foo()
# print(result)
#返回值可以不只有一个
# def multi_value():
#     r1=1
#     r2=2
#     r3=3
#     r4=4
#     return r1,r2,r3,r4
# s=multi_value()
# print(s)
#利用元组给多个变量赋值
# def two_value():
#     return "hh","ss"
# r1,r2=two_value()
# print(r1)
# print(r2)
#lambda表达式就是不想费神命函数名
# f=lambda x,y:x+y
# print(f)
# z=f(1,2)
# print(z)
#filter
# l1=[1,2,3,4,5,6,7,8]
# l2=[item for item in filter(lambda x:x>5,l1)]
# print(l2)
# def add(x,y):
#     """
#     返回参数x和y的两数之和
#     :parameters
#     -----------------
#     x : int
#     第一个参数
#     y:int
#     第二个参数
#     :Returns
#     ----------------
#     int 返回x+y
#     :param x:
#     :param y:
#     :return:
#     """
#     return x+y
# print(add(1,2))
# print(add.__doc__)
#函数注释
# def compile(source:"管大爷",filename:"李耀华",mode:"净资产")->bool:
#     return True
# print(compile.__annotations__)
