x=True
if x:
    print("管大爷最帅！")
x=18;#如果为0也是false
if x:
    print("x is",x)
x="hello"
if x:
    print("x is",x)
x=""#如果字符串为空就是false
if x:
    print("x is",x)
s=0
if s: print("s is",s)
else : print("s is 0")
#空列表 元组，字典也是false
d=89
x=1
while x<=10:
    print("x is ",x)
    x+=1
# if d>90:
#     print("优")
# elif d>80:
#     print("良")
# elif d>60:
#     print("及格")
# else :
#     print("hello")
# for x in (1,2,3,4,5,6,7,8):
#     print("x is ",x)
# for x in(0,1,2):
#     print("hello world!")
# for x in range(10):
#     print("hahah")
# for x in range(1,10):
#     print(x)
# for x in range(1,10,2): 三个参数分别为开始，结束，步长
#     print(x)
# for i in range(10):
#     if i>5:
#         break
#     else:
#         print(i)
# for i in range(10):
#     if i==5:
#         continue
#     else:
#         print(i)
#pass
# for i in range(10):
#     if i==3:
#         pass
#     else:
#         print(i)
#循环中的else
count=0
# while count<5:
#     print(count,"is less than 5")
#     count+=1
# else:
#     print("count","is not less than 5")
for count in range(5):
    print(count,"in for segment")
else:
    print(count,"in else segment")