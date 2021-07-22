# def fib(n):
#     a,b=0,1
#     while b<n:
#         print(b,end=' ')
#         a,b=b,a+b
#     print()
# def fib2(n):
#     result=[]
#     a,b=0,1
#     while b<n:
#         result.append(b)
#         a,b=b,b+a
#     return result
#标准库
import sys
# print(sys.platform)
# print(sys.argv)
# if len(sys.argv)<=1:
#     print("少了")
#     sys.exit(1)
# for arg in sys.argv:
#     print(arg)
# for path in sys.path:
#     print(path)
# import sys
# print(sys.modules.keys())
# print(sys.modules.values())
# print(sys.modules["os"])
#math
# import math
# print("圆周率",math.pi)
# print("自然常数",math.e)
# print("\n向上取整")
# print("1.7",math.ceil(1.7))
# print("0.3",math.ceil(0.3))
# print("-1.7",math.ceil(-1.7))
# print("-0.3",math.ceil(-0.3))
# print("\n向下取整")
# print("1.7",math.floor(1.7))
# print("0.3",math.floor(0.3))
# print("-1.7",math.floor(-1.7))
# print("-0.3",math.floor(-0.3))
# print("\n指数运算")
# print("15^3",math.pow(15,3))
# print("29^-1",math.pow(29,-1))
# print("\n对数计算,默认以e为底，第二个参数修改底")
# print("log(3)",math.log(3))
# print("log(100,10)",math.log(100,10))
# print("\n平方根")
# print("sqrt(4)",math.sqrt(4))
# print("sqrt(128)",math.sqrt(128))
# print("\n三角函数")
# print("sin(pi/2)",math.sin(math.pi/2))
# print("cos(pi)",math.cos(math.pi))
# print("tan(0)",math.tan(0))
# print("\n随机数")
# import random
# print(random.random())
# print(random.uniform(1,150))
# print(random.randint(1,150))
# seq1=(1,15,144,34,22)
# seq2=["星期一","星期二","星期三","星期四"]
# print(random.choice(seq1))
# print(random.choice(seq2))
# random.shuffle(seq1)
# random.shuffle(seq2)