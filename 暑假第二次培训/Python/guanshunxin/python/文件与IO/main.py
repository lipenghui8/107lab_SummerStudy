# file_name="mo.py"
# f=open(file_name)
# f=open("read.txt")
# text=f.read()
# print(text)
# f=open("white.txt","w")
# txt="管大爷"
# print(f.write(txt))
# from datetime import datetime
# f=open("read.txt","a")
# now=str(datetime.now())+"\n"
# print(f.write(now))
# h=open("read.txt")
# txt=h.read()
# print(txt)
# f=open("read.txt","r")
# print(f.readline())
# print(f.readline())
# for line in f.readlines():
#     print(line)
# for line in f:
#     print(line)
# f=open("white.txt","w")
# lines=[]
# for i in range(10):
#     lines.append(str(i)+"\n")
# f.writelines(lines)
# f.close()
# with open("white.txt","r") as f:
#     content=f.read
#     print(content)
#stringIO和BytesIO
# from io import StringIO
# f=StringIO()
# f.write("hello")
# f.write(" ")
# f.write("world!")
# print(f.getvalue())
# from io import StringIO
# f=StringIO("hello!\nWorld\nWelcome!")
# while True:
#     s=f.readline()
#     if s=="":
#         break
#     print(s.strip())
#BytesIO
# from io import BytesIO
# f=BytesIO()
# f.write("您好".encode("utf-8"))
# print(f.getvalue())
# print(f.getvalue().decode("utf-8"))
# from io import BytesIO
# f=BytesIO(b'\xe6\x82\xa8\xe5\xa5\xbd')
# print(f.read().decode("utf-8"))
# import pickle
# class Student:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
# student1=Student("小红",12,"女")
# with open("student1.data","wb") as f:
#     pickle.dump(student1,f)
# f=open("student1.data","rb")
# data=f.read()
# student1=pickle.loads(data)
# f.close()
# print("姓名：",student1.name)
# print("年龄：",student1.age)
# print("性别：",student1.gender)
# with open("student1.data","rb") as f:
#     student1=pickle.load(f)
#     print("姓名：",student1.name)
#     print("年龄：",student1.age)
#     print("性别：",student1.gender)
# import json
# student1={
#     "name":"金子淳",
#     "age":"99",
#     "gender":"女"
# }
# print(json.dumps(student1))
# with open("student1.json","w") as f:
#     json.dump(student1,f)
# with open("student1.json","r") as f:
#     student1=json.load(f)
#     print(student1)
