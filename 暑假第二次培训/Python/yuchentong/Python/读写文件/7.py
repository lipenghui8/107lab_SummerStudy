with open('test.txt','a+') as f:
    f.seek(0)
    s=f.readlines()
    print(s)
    f.seek(2)
    f.writelines(s)