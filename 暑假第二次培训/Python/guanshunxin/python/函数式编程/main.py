import math
from functools import reduce
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,9,abs))
def add1(a,b,c):
    return c(a)+c(b)
print(add1(1,2,math.sqrt))
#map
def f(x):
    return x*x
for item in map(f,[1,2,3,4,5,6,7,8,9]):
    print(item)
#reduce
def f(x,y):
    return x+y
print(reduce(f,[1,3,5,7,9]))
#filter
def is_odd(x):
    return x%2==1
for item in filter(is_odd,[1,4,6,7,9,23,12]):
    print(item)
def is_not_empty(s):
    return s and len(s.strip())>0
for item in filter(is_not_empty,["test",None,'','str','  ','END']):
    print(item)
s="   111"
print(s.strip())
s='\t\t123\r\n'
print(s.strip())
def is_zheng(x):
    r=int(math.sqrt(x))
    return r*r==x
for item in filter(is_zheng,range(1,101)):
    print(item)
#自定义排序函数
print(sorted([35,12,3,2,11,7]))
score=[('Alice',399),('blice',44),('clice',35)]
print(sorted([('Alice',33),('blice',44),('clice',55)]))
def k(item):
    return item[1]
print(sorted(score,key=k))
print(sorted(score,key=k,reverse=True))
def k(item):
    return item.lower()
print(sorted(['bob','about','Zoo','Creied'],key=k))
#返回函数
def func():
    def sub_func():
        print('call')
    sub_func()
func()
def f():
    print('call f()..')
    def g():
        print('call g()...')
    return g
print(f())
x=f()
x()
f()
#直接计算
def cal_sum(list_):
    return sum(list_)
print(cal_sum(([1,2,3,4])))
#延迟计算
def calc_sum(list_):
    def lazy_sum():
        return sum(list_)
    return lazy_sum
f=calc_sum(([1,2,3,4]))
print(f)
print(f())
def cheng(list_):
    s=1
    for item in list_:
        s*=item
    return s
print(cheng([1,2,3,4]))
def cal_prod(list_):
    def lazy_prod():
        def f(x,y):
            return x*y
        return reduce(f,list_)
    return lazy_prod
f=cal_prod([1,2,3,4])
print(f())
#闭包
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f(i))
#     return fs
# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())
#所以不要在里面引用变化的量
def count():
    fs = []
    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
#匿名函数
result=[item for item in map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])]
print(result)
print(reduce(lambda x,y:x+y,[1,3,5,7,9]))
print(sorted(['bob','about','Zoo','Creied'],key=lambda item:item.lower()))
def log(f):
    def fn(x):
        print('call'+f.__name__+'()...')
        return f(x)
    return fn
@log
def fac(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(fac(10))
import time
def performance(f):
    def fn(*args,**kw):
        t1=time.time()
        r=f(*args,**kw)
        t2=time.time()
        print('call %s() in %fs'%(f.__name__,(t2-t1)))
        return r
    return fn
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))
import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            r = f(*args, **kwargs)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call {}() in {} {}'.format(f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
factorial(10)
print(int('12345'))
print(int('12345',base=8))
print(int('12345',16))
def int2(x,base=2):
    return int(x,base)
print(int2('1000000'))
print(int2('1010101'))
#partial
import functools
int3=functools.partial(int,base=2)
print(int3('1000000'))
print(int3('1010101'))
sorted_ignore=functools.partial(sorted,key=lambda item:item.lower())
print(sorted_ignore(['bob','about','Zoo','Cred']))
