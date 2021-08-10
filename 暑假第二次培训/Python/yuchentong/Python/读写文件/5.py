f=open('test.txt','r')
s1=f.readlines()
f1=open('test1.txt','w')
for s in s1:
    s=s[::-1]
    f1.write(s)
f1.close()
f.close()